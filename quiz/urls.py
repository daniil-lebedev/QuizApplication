from django.urls import path

from . import views

urlpatterns = [
    path("create_quiz", views.create_quiz, name="create_quiz"),
    path("quiz_management/<int:quiz_id>/", views.quiz_management, name="quiz_management"),
    path("view_quiz/<int:quiz_id>/", views.view_quiz, name="view_quiz"),
    path("add_question/<int:quiz_id>/", views.add_question, name="add_question"),
    path("quiz_edit/<int:quiz_id>/", views.quiz_edit, name="quiz_edit"),
    path("edit_question/<int:quiz_id>/<int:question_id>/", views.edit_question, name="edit_question"),
    path("create_option/<int:quiz_id>/<int:question_id>/", views.create_option, name="create_option"),
    path("edit_option/<int:quiz_id>/<int:question_id>/<int:option_id>/", views.edit_option, name="edit_option"),
    path("take_quiz/<int:team_id>/<int:quiz_id>", views.take_quiz, name="take_quiz"),
    path("view_result/<int:quiz_id>/<int:team_id>/", views.view_result, name="view_result"),
    path("view_quiz_analysis/<int:quiz_id>/<int:team_id>", views.view_quiz_analysis,
         name="view_quiz_analysis"),
    path("delete_quiz/<int:quiz_id>/", views.delete_quiz, name="delete_quiz"),
]
