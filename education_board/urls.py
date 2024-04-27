from django.urls import path
from .views import view_all_boards, create_board, create_slide, board_detail, delete_board, edit_board

urlpatterns = [
    path('view_all_boards/', view_all_boards, name='view_all_boards'),
    path('create_board/', create_board, name='create_board'),
    path('board/<int:board_id>/create_slide/', create_slide, name='create_slide'),
    path('board/<int:board_id>/', board_detail, name='board_detail'),
    path('delete_board/<int:board_id>/<int:team_id>', delete_board, name='delete_board'),
    path('edit_board/<int:board_id>', edit_board, name='edit_board'),
]
