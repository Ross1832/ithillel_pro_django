from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.datetime_safe import date
from .validators import ValidEmailDomain, validate_phone_number
from dateutil.relativedelta import relativedelta
from groups.models import Groups
from faker import Faker


VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com')


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='first name', db_column='first_name',
                                  validators=[MinLengthValidator(2, '"first_name" field value less then two symbols')])
    last_name = models.CharField(max_length=100, verbose_name='last name', db_column='_last_name',
                                 validators=[MinLengthValidator(2)],
                                 error_messages={'min_length': '"last_name" field value less then two symbols'})
    birthday = models.DateField(default=date.today, null=True, blank=True)
    email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)], default=None)
    phone = models.CharField(max_length=15, verbose_name='phone number', db_column='phone_number',
                             validators=[validate_phone_number], default=None)

    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, related_name='students')
    create_datetime = models.DateTimeField(auto_now_add=True, null=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.group is None:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name} {self.last_name} ({self.group.name})'

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    class Meta:
        db_table = 'student_table'
        verbose_name_plural = "Students"

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print(f'Incorrect data {first_name}, {last_name}, {email}, {birthday}')
