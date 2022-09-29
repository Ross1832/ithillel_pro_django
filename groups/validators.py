from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date


def validate_start_date(value):
    if value < date.today():
        raise ValidationError("Start date cannot be in the past")
