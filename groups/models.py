from django.db import models
from django.utils.datetime_safe import date


class Groups(models.Model):
    name_group = models.CharField(max_length=100, null=False, blank=False)
    data_start = models.DateField(default=date.today, null=False, blank=False)
    description = models.TextField()
    