from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models

from core.validators import ValidEmailDomain


class BaseModel(models.Model):
    create_datetime = models.DateTimeField(auto_now=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')

    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years
