from django.urls import path
from .views import (get_students,
                    create_student,
                    update_student,
                    detail_student,
                    delete_student,)

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('detail/<int:student_id>/', detail_student, name='detail'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
