from django import forms
from .models import Course
from django_filters import FilterSet


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CourseCreateForm(CourseBaseForm):
    from groups.models import Groups

    class Meta(CourseBaseForm.Meta):
        pass


class CourseUpdateForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains']
        }
