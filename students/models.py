from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.datetime_safe import date
from .validators import ValidEmailDomain, validate_unique_email, validate_phone_number
from dateutil import relativedelta


VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com')


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='first name', db_column='first_name',
                                  validators=[MinLengthValidator(2, '"first_name" field value less then two symbols')])
    last_name = models.CharField(max_length=100, verbose_name='last name', db_column='_last_name',
                                 validators=[MinLengthValidator(2)],
                                 error_messages={'min_length': '"last_name" field value less then two symbols'})
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST), validate_unique_email], default=None)
    phone = models.CharField(max_length=15, verbose_name='phone number', db_column='phone_number',
                             validators=[validate_phone_number], default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'student_table'
        verbose_name_plural = "Students"
