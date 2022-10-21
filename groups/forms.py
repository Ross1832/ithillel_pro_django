from django import forms
from .models import Groups
from django_filters import FilterSet


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = [
            'name_group',
            'data_start',
            'description',
        ]

        widgets = {
            'data_start': forms.DateInput(attrs={'type': 'date'})
        }


class GroupFilterForm(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'name_group': ['exact', 'icontains']
        }
