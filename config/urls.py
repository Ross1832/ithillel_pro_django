from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls', namespace='students')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
    path('course/', include('course.urls', namespace='course')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
