from django.urls import path
from .views import get_students, create_student, update_student, detail_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='students'),
    path('create/', create_student, name='create_student'),
    path('update/<int:student_id>/', update_student, name='update_student'),
    path('detail/<int:student_id>/', detail_student)
]
