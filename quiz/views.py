from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.db.models import Avg

from company.models import TeamAdmin, Member, Team
from .forms import CreateQuizForm, CreateQuestionForm, CreateOptionForm
from .models import Quiz, Question, Option, Result


@login_required
def create_quiz(request):
    if request.method == "POST":
        form = CreateQuizForm(request.POST, user=request.user)
        if form.is_valid():
            quiz = form.save(commit=False)
            # Assuming 'belongs_to' is a Team instance
            selected_team = form.cleaned_data.get("belongs_to")
            # Verify the current user is an admin of the selected team
            try:
                team_admin = TeamAdmin.objects.get(team=selected_team, user=request.user)
                quiz.author = team_admin
                quiz.belongs_to = selected_team  # Assuming you have a belongs_to field in your Quiz model
                quiz.save()
                return redirect("quiz_management", quiz_id=quiz.id)
            except TeamAdmin.DoesNotExist:
                return HttpResponse("You are not an admin of the selected team.", status=403)
    else:
        form = CreateQuizForm(request.user)

    return render(request, "quiz/create_quiz.html", {"form": form})


@login_required
def take_quiz(request, team_id, quiz_id):
    team = get_object_or_404(Team, id=team_id)
    quiz = get_object_or_404(Quiz, id=quiz_id, belongs_to=team)

    if timezone.now() > quiz.due_date:
        messages.error(request, "This quiz is no longer available.")
        return redirect('home')  # Adjust as needed

    if not Member.objects.filter(team=team, user=request.user).exists():
        messages.error(request, "You are not authorized to take this quiz.")
        return redirect('user_profile')  # Adjust as needed

    team_member = Member.objects.get(team=team, user=request.user)

    if request.method == 'POST':
        score = 0

        for question in quiz.question_set.all():
            # Extract the chosen option ID from POST data for each question
            chosen_option_id = request.POST.get(str(question.id))
            if chosen_option_id:
                chosen_option = Option.objects.filter(id=chosen_option_id, question=question).first()
                if chosen_option and chosen_option.is_correct:
                    score += chosen_option.point  # Add the option's point value to the score

        # Save the result with the calculated score
        result = Result.objects.create(quiz=quiz, user=team_member, score=score, date_taken=timezone.now())
        result.save()
        messages.success(request, "Your quiz results have been saved.")
        return redirect('view_result', quiz_id=quiz_id, team_id=team_id)

    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'team': team})


@login_required
def quiz_management(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, belongs_to__admins=request.user)
    quiz.update_points()
    # get the questions for this quiz
    questions = Question.objects.filter(quiz=quiz)
    context = {
        'quiz_id': quiz.id,
        'quiz_name': quiz.title,
        'quiz': quiz,
        'questions': questions,
    }

    return render(request, 'quiz/quiz_management.html', context)


@login_required
def quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, belongs_to__admins=request.user)
    if request.method == 'POST':
        form = CreateQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            # Redirect to the quiz management page or wherever you see fit
            return redirect('quiz_management', quiz_id=quiz.id)
    else:
        form = CreateQuizForm(instance=quiz)

    quiz.update_points()

    return render(request, 'quiz/quiz_edit.html', {'form': form, 'quiz_id': quiz.id})


@login_required
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, belongs_to__admins=request.user)

    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            question.update_point()
            return redirect('quiz_management', quiz_id=quiz_id)
    else:
        form = CreateQuestionForm()
    quiz.update_points()
    return render(request, 'quiz/add_question.html', {'form': form, 'quiz_id': quiz_id})


@login_required
def edit_question(request, quiz_id, question_id):
    # Ensure the user has rights to edit the question, e.g., by checking if they're the quiz owner/admin
    question = get_object_or_404(Question, id=question_id, quiz__id=quiz_id, quiz__belongs_to__admins=request.user)
    form = CreateQuestionForm(instance=question)
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            # Redirect to the quiz management page or to the quiz editing page
            return redirect('quiz_management', quiz_id=quiz_id)
    question.update_point()

    return render(request, 'quiz/edit_question.html', {'form': form, 'quiz_id': quiz_id, 'question_id': question_id})


@login_required
def create_option(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz__id=quiz_id, quiz__belongs_to__admins=request.user)

    if request.method == 'POST':
        form = CreateOptionForm(request.POST)
        if form.is_valid():
            # Save the new option instance but don't commit to DB yet
            new_option = form.save(commit=False)
            new_option.question = question  # Set the question foreign key
            new_option.save()  # Save the new option to the DB
            question.update_point()
            return redirect('quiz_management', quiz_id=quiz_id)  # Redirect to the quiz management page
    else:
        form = CreateOptionForm()

    return render(request, 'quiz/create_option.html', {'form': form, 'question': question})


@login_required
def edit_option(request, quiz_id, question_id, option_id):
    option = get_object_or_404(Option, id=option_id, question_id=question_id, question__quiz__id=quiz_id,
                               question__quiz__belongs_to__admins=request.user)

    if request.method == 'POST':
        form = CreateOptionForm(request.POST, instance=option)
        if form.is_valid():
            form.save()  # Save changes to the option
            return redirect('quiz_management', quiz_id=quiz_id)  # Redirect to the quiz management page
    else:
        form = CreateOptionForm(instance=option)

    return render(request, 'quiz/edit_option.html', {'form': form, 'option': option})


@login_required
def show_all_quizzes(request):
    quizzes = Quiz.objects.filter(belongs_to__admins=request.user)
    return render(request, 'quiz/show_all_quizzes.html', {'quizzes': quizzes})


@login_required
def view_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, belongs_to__admins=request.user)
    return render(request, 'quiz/view_quiz.html', {'quiz': quiz})


@login_required
def view_result(request, quiz_id, team_id):
    """
    Show user the result of the quiz they took.
    :param request: request for the page
    :param quiz_id: ID of the quiz
    :param team_id: ID of the team
    :param user_id: ID of the user
    :return: HttpResponse object with the quiz result
    """
    quiz = get_object_or_404(Quiz, id=quiz_id)
    team = get_object_or_404(Team, id=team_id)
    user = get_object_or_404(request.user.__class__, id=request.user.id)
    member = get_object_or_404(Member, user=user, team=team)

    result = get_object_or_404(Result, quiz=quiz, user=member)
    total_points = quiz.points
    score = result.score
    percentage = (score / total_points * 100) if total_points > 0 else 0

    context = {
        'result': result,
        'percentage': percentage,
        'quiz': quiz,
        'team': team,
        'member': member
    }
    return render(request, 'quiz/view_result.html', context)


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, Team, Result, Member
from django.db.models import Avg


@login_required
def view_quiz_analysis(request, quiz_id, team_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    team = get_object_or_404(Team, id=team_id)

    if not team.team_of_admin.filter(user=request.user).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    total_members = Member.objects.filter(team=team).count()
    participants = Result.objects.filter(quiz=quiz, user__team=team).count()
    average_score = Result.objects.filter(quiz=quiz, user__team=team).aggregate(Avg('score'))['score__avg'] or 0
    detailed_results = Result.objects.filter(quiz=quiz, user__team=team).select_related('user')

    participation_rate = (participants / total_members * 100) if total_members > 0 else 0

    context = {
        'quiz': quiz,
        'team': team,
        'total_members': total_members,
        'participants': participants,
        'average_score': average_score,
        'detailed_results': detailed_results,
        'participation_rate': participation_rate
    }
    return render(request, 'quiz/view_quiz_analysis.html', context)
