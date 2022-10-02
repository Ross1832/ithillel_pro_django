from django.urls import path
from .views import index, get_students, create_student, update_student, detail_student

app_name = 'students'

urlpatterns = [
    path('', index, name='index'),
    path('students/', get_students, name='students'),
    path('students/create/', create_student, name='create_student'),
    path('students/update/<int:student_id>/', update_student, name='update_student'),
    path('students/detail/<int:student_id>/', detail_student)
]
