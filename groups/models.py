import datetime

from django.db import models
from core.models import BaseModel
from teachers.models import Teacher


class Groups(BaseModel):
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
    teachers = models.ManyToManyField(
        to=Teacher,

        blank=True,
        related_name='groups'
    )

    class Meta:
        verbose_name_plural = 'Groups'
        db_table = 'groups'

    def __str__(self):
        return f'Group name: <{self.name_group}>'
