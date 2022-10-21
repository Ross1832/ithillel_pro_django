import datetime

from django.db import models
from django.utils import timezone

from .validators import validate_start_date


class Groups(models.Model):
    name_group = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    start_date = models.DateField(default=datetime.datetime.utcnow)
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Groups'
        db_table = 'groups'

    def __str__(self):
        return f'Group name: <{self.name_group}>'
