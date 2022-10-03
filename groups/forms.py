from django import forms
from .models import Groups


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



