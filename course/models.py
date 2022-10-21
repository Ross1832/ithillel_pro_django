from django.db import models
import datetime


class Course(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    start_date = models.DateField(default=datetime.datetime.utcnow)
    end_date = models.DateField(null=True, blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    update_datetime = models.DateTimeField(auto_now=True)
    group = models.OneToOneField(
        'groups.Groups',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses',
    )

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'Course name: <{self.name}>'
