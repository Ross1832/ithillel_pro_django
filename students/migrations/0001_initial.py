# Generated by Django 4.1 on 2022-09-29 10:37

import django.core.validators
from django.db import migrations, models
import django.utils.datetime_safe
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" field value less then two symbols')], verbose_name='first name')),
                ('last_name', models.CharField(db_column='_last_name', error_messages={'min_length': '"last_name" field value less then two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('birthday', models.DateField(blank=True, default=django.utils.datetime_safe.date.today, null=True)),
                ('email', models.EmailField(default=None, max_length=254, validators=[students.validators.ValidEmailDomain('@gmail.com', '@yahoo.com'), students.validators.validate_unique_email])),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'student_table',
            },
        ),
    ]
