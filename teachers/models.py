from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    date_of_birth = models.DateField()
    start_date_of_work = models.DateField()
    phone = models.PositiveIntegerField(null=True)
