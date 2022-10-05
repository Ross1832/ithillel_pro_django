from django.urls import path
from .views import get_groups, create_group, update_group, detail_group, delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:group_id>/', update_group, name='update'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
