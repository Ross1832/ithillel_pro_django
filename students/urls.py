from django.urls import path
from .views import index, get_students, create_student

app_name = 'students'

urlpatterns = [
    path('', index, name='index'),
    path('students/', get_students, name='students'),
    path('students/create/', create_student, name='create_s'),
]
