from django.db import models
from .validators import validate_start_date


class Groups(models.Model):
    name_group = models.CharField(max_length=100, null=False, blank=False)
    data_start = models.DateField(validators=[validate_start_date], null=False,
                                  blank=False,)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Groups'
