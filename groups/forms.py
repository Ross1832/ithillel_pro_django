from django import forms
from .models import Groups
from django_filters import FilterSet


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class GroupCreateForm(GroupBaseForm):
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), requred=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(GroupBaseForm.Meta):
        pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'name_group': ['exact', 'icontains']
        }
