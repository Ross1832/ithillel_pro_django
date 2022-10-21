from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Course
from .forms import CourseCreateForm, CourseUpdateForm, CourseFilterForm


def get_courses(request):
    courses = Course.objects.select_related('group')

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)

    context = {
        'title': 'list of courses',
        'courses': courses,
        'filter_form': filter_form,
    }
    return render(request, 'course/list.html', context)


def create_courses(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    elif request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))
    context = {
        'form': form,
    }
    return render(request, 'course/create.html', context)


def update_courses(request, course_id):
    courses = get_object_or_404(Course, pk=course_id)

    if request.method == "GET":
        form = CourseUpdateForm(instance=courses)
    elif request.method == "POST":
        form = CourseUpdateForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))
    context = {
        'form': form,
    }
    return render(request, 'course/update.html', context)


def detail_courses(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course
    }
    return render(request, 'course/detail.html', context)


def delete_courses(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        course.delete()
        return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'course/delete.html', {'course': course})
