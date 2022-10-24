from django.urls import path
from .views import (ListStudentView,
                    CreateStudentView,
                    UpdateStudentView,
                    DetailStudentView,
                    DeleteStudentView,)

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
]

