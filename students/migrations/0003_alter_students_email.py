# Generated by Django 4.1 on 2022-09-27 13:28

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_email_alter_students_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(default=None, max_length=254, validators=[students.validators.ValidEmailDomain('@gmail.com', '@yahoo.com')]),
        ),
    ]
