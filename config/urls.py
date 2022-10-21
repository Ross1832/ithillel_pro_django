from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls', namespace='students')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
