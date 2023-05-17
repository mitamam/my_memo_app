from django.urls import path

from . import views

app_name = 'memos'
urlpatterns = [
    # ex. /memos/
    path('', views.index, name='index'),
    # ex. /memos/create/
    path('create/', views.create, name='create'),
    # ex. /memos/{memo_id}/edit
    path('<int:memo_id>/edit/', views.edit, name='edit'),
    # ex. /memos/{memo_id}/delete/
    path('<int:memo_id>/delete/', views.delete, name='delete'),
]
