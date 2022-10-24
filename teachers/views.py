from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

from .models import Teacher
from .forms import TeacherForm, TeacherFilterForm


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list_of_teachers.html'
    context_object_name = 'teachers'


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/update.html'
    success_url = reverse_lazy('teachers:list')


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')