from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str
from django.db.models import Q

from .models import Teacher
from .forms import TeacherForm


@use_args({
    'name': Str(required=False),
    'surname': Str(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) != 0 and args.get('name') or args.get('surname'):
        teachers = teachers.filter(
            Q(name=args.get('name', '')) | Q(surname=args.get('surname', ''))
        )

    context = {
        "title": "List of Teachers",
        "teachers": teachers,
    }
    return render(request, 'teachers/list_of_teachers.html', context)


def create_teacher(request):
    if request.method == "GET":
        form = TeacherForm()
    elif request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/create.html', {'form': form})


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == "GET":
        form = TeacherForm(instance=teacher)
    elif request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/update.html', {'form': form})


def detail_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {
        'teacher': teacher
    }
    return render(request, 'teachers/detail.html', context)


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/delete.html', {'teacher': teacher})
