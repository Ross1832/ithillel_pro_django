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
    def __init__(self, *args, **kwargs):
        from students.models import Student
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            queryset=Student.objects.select_related('group'),
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'headman'
        ]


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False,
        )
        self.fields['headman_field'].choices.insert(0, (0, '--------'))

    class Meta(GroupBaseForm.Meta):
        exclude = (
            'start_date',
            'headman'
        )


class GroupFilterForm(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'name_group': ['exact', 'icontains']
        }
