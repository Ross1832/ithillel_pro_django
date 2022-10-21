from django import forms
from django_filters import FilterSet
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'name',
            'surname',
            'date_of_birth',
            'start_date_of_work',
            'phone'
        ]

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'start_date_of_work': forms.DateInput(attrs={'type': 'date'}),
        }


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'name': ['exact', 'icontains'],
            'surname': ['exact', 'startswith'],
        }
