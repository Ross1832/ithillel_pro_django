from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from .models import Course
from .forms import CourseCreateForm, CourseUpdateForm, CourseFilterForm


class ListCourseView(ListView):
    model = Course
    template_name = 'course/list.html'
    context_object_name = 'courses'


class UpdateCourseView(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = 'course/update.html'
    success_url = reverse_lazy('course:list')


class DetailCourseView(DetailView):
    model = Course
    template_name = 'course/detail.html'
    context_object_name = 'course'


class CreateCourseView(CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'course/create.html'
    success_url = reverse_lazy('course:list')


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'course/delete.html'
    success_url = reverse_lazy('course:list')
