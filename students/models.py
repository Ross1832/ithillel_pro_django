from django.db import models
from groups.models import Groups
from core.models import PersonModel


class Student(PersonModel):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, related_name='students')

    def __str__(self):
        if self.group is None:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name} {self.last_name} ({self.group.name_group})'

    class Meta:
        verbose_name_plural = "Students"

