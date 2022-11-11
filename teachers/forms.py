from django import forms
from django_filters import FilterSet
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'start_date_of_work',
            'phone'
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'start_date_of_work': forms.DateInput(attrs={'type': 'date'}),
        }


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
