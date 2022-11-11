from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView
from .models import Student
from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from core.views import CustomUpdateBaseView


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    paginate_by = 2

    def get_filter(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)
        return filter_form

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_filter().form
        context['counter'] = 0
        return context


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = CreateStudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')
