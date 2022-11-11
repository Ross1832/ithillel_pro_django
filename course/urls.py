from django.urls import path
from .views import (ListCourseView,
                    CreateCourseView,
                    UpdateCourseView,
                    DetailCourseView,
                    DeleteCourseView,)

app_name = 'course'

urlpatterns = [
    path('', ListCourseView.as_view(), name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateCourseView.as_view(), name='update'),
]
