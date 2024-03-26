from django.urls import path

from . import views

urlpatterns = [
    path("create_quiz", views.create_quiz, name="create_quiz"),
    path("quiz_management/<int:quiz_id>/", views.quiz_management, name="quiz_management"),
    path("view_quiz/<int:quiz_id>/", views.view_quiz, name="view_quiz"),
    path("show_all_quizzes", views.show_all_quizzes, name="show_all_quizzes"),
    path("add_question/<int:quiz_id>/", views.add_question, name="add_question"),
    path("quiz_edit/<int:quiz_id>/", views.quiz_edit, name="quiz_edit"),
    path("edit_question/<int:quiz_id>/<int:question_id>/", views.edit_question, name="edit_question"),
    path("create_option/<int:quiz_id>/<int:question_id>/", views.create_option, name="create_option"),
    path("edit_option/<int:quiz_id>/<int:question_id>/<int:option_id>/", views.edit_option, name="edit_option"),
]
