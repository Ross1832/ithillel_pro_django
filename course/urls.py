from django.urls import path
from .views import (get_courses,
                    create_courses,
                    update_courses,
                    detail_courses,
                    delete_courses,)

app_name = 'course'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_courses, name='create'),
    path('update/<int:course_id>/', update_courses, name='update'),
    path('detail/<int:course_id>/', detail_courses, name='detail'),
    path('delete/<int:course_id>/', delete_courses, name='delete'),
]
