from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from company.models import Team, TeamAdmin
from quiz.models import Quiz
from .models import Board
from .forms import CreateBoardForm, CreateSlideForm


@login_required
def view_all_boards(request) -> render:
    """
    Function to view all the education boards.

    Args:
    request: The request object.

    Returns:
    A response object with the list of all the education boards.
    """
    # get all the boards
    boards = Board.objects.all()
    return render(request, 'education_board/view_all_boards.html', {'boards': boards})


@login_required
def create_board(request) -> render:
    if request.method == 'POST':
        form = CreateBoardForm(request.POST, user=request.user)
        if form.is_valid():
            try:
                form.save()
                return redirect('view_all_boards')  # Redirect to a success page
            except Exception as e:
                form.add_error(None, e)
    else:
        form = CreateBoardForm(user=request.user)

    return render(request, 'education_board/create_board.html', {'form': form})


@login_required
def board_detail(request, board_id) -> render:
    try:
        board = Board.objects.get(id=board_id)  # Verify the board exists
        # get all the slides for the board
        slides = board.slides.all()
        # get the quiz for the board
        try:
            quiz = Quiz.objects.get(educational_board_id=board.id)
        except Quiz.DoesNotExist:
            quiz = None
    except Board.DoesNotExist:
        messages.error(request, "Board does not exist.")
        return redirect('view_all_boards')

    return render(request, 'education_board/board_detail.html', {'board': board, 'slides': slides, 'quiz': quiz})


@login_required
def create_slide(request, board_id) -> redirect:
    try:
        board = Board.objects.get(id=board_id)  # Verify the board exists
    except Board.DoesNotExist:
        messages.error(request, "Board does not exist.")
        return redirect('view_all_boards')

    if request.method == 'POST':
        form = CreateSlideForm(request.POST, board_id=board_id)
        if form.is_valid():
            form.save()
            return redirect('board_detail', board_id=board_id)  # Adjust redirect as necessary
    else:
        form = CreateSlideForm(board_id=board_id)

    return render(request, 'education_board/create_slide.html', {'form': form, 'board': board})


@login_required
def delete_board(request, board_id: int, team_id: int) -> redirect or render:
    """
    Deletes a specific educational board.
    :param team_id: ID of the Team to which the board belongs
    :param request: HttpRequest object
    :param board_id: ID of the Board to delete
    :return: Redirects to a success or fallback URL
    """
    board = get_object_or_404(Board, id=board_id)
    # get the team
    team = get_object_or_404(Team, id=team_id)
    # get the team admin
    team_admin = TeamAdmin.objects.filter(user=request.user, team=team)
    # Check if the request.user is authorized to delete the board
    if team_admin != board.created_by:
        messages.error(request, "You do not have permission to delete this board.")

    if request.method == 'POST':
        board.delete()
        messages.success(request, "Board deleted successfully.")
        return redirect('view_team_as_admin', team.id)  # Redirect to the list of boards or another appropriate view

    return render(request, 'education_board/confirm_delete.html', {'board': board, 'team': team})


@login_required
def edit_board(request, board_id) -> render or redirect:
    board = get_object_or_404(Board, id=board_id)

    # Check permission
    if not board.team.team_of_admin.filter(user=request.user).exists():
        messages.error(request, "You do not have permission to edit this board.")
        return redirect('boards_list')  # Or wherever you list boards

    if request.method == 'POST':
        form = CreateBoardForm(request.POST, instance=board, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Board updated successfully.")
            return redirect('board_detail', board_id=board.id)
    else:
        form = CreateBoardForm(instance=board, user=request.user)

    return render(request, 'education_board/edit_board.html', {'form': form, 'board': board})
