from django.urls import path
from .views import ListTeacherView, CreateTeacherView, UpdateTeacherView, DetailTeacherView, DeleteTeacherView

app_name = 'teachers'

urlpatterns = [
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete'),
    path('', ListTeacherView.as_view(), name='list'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail')
]
