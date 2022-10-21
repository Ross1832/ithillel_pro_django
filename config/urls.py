from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('students/', include('students.urls', namespace='students')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
    path('course/', include('course.urls', namespace='course')),
    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
