from django import forms
from django_filters import FilterSet

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        correct_order = str(value[0]).upper() + str(value[1:]).lower()
        return correct_order

    def clean_last_name(self):
        value = self.cleaned_data['last_name']
        correct_order = str(value[0]).upper() + str(value[1:]).lower()
        return correct_order

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number']
        return "".join(i for i in value if i in "0123456789-()")


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
