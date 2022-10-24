from django.db import models
from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=10000)
    start_date_of_work = models.DateField()
    phone = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'
