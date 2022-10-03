from django.urls import path
from .views import get_teachers, create_teacher, update_teacher, detail_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers),
    path('create/', create_teacher),
    path('update/<int:teacher_id>/', update_teacher),
    path('detail/<int:teacher_id>/', detail_teacher),
]
