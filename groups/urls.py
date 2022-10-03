from django.urls import path
from .views import get_groups, create_group, update_group, detail_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='groups'),
    path('create/', create_group),
    path('update/<int:group_id>/', update_group),
    path('detail/<int:group_id>/', detail_group),
]
