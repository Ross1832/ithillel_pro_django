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
    context_object_name = 'students'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'


class CreateStudentView(CreateView):
    model = Student
    form_class = CreateStudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')
