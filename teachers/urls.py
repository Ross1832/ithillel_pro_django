from django.urls import path
from .views import get_teachers, create_teacher, update_teacher, detail_teacher, delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
