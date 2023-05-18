from django.urls import path

from . import views

app_name = 'memos'
urlpatterns = [
    # ex. /memos/
    path('', views.memo_list_view, name='memo-list'),
    # ex. /memos/create/
    path('create/', views.memo_create_view, name='memo-create'),
    # ex. /memos/{memo_id}/edit
    path('<int:memo_id>/edit/', views.memo_edit_view, name='memo-edit'),
    # ex. /memos/{memo_id}/delete/
    path('<int:memo_id>/delete/', views.memo_delete_view, name='memo-delete'),
]
