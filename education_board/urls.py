from django.urls import path
from .views import view_all_boards, create_board, create_slide, board_detail

urlpatterns = [
    path('view_all_boards/', view_all_boards, name='view_all_boards'),
    path('create_board/', create_board, name='create_board'),
    path('board/<int:board_id>/create_slide/', create_slide, name='create_slide'),
    path('board/<int:board_id>/view_detail', board_detail, name='board_detail'),
]
