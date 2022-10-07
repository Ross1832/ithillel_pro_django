from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
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


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
