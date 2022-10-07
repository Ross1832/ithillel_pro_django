from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str
from .models import Student
from .forms import CreateStudentForm, UpdateStudentForm


@use_args({
    'first_name': Str(required=False),
    'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    context = {
        'title': 'LIST OF STUDENTS',
        'students': students,
    }
    return render(request, 'students/list.html', context)


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    context = {
        'form': form,
    }
    return render(request, 'students/create.html', context)


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "GET":
        form = UpdateStudentForm(instance=student)
    elif request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    context = {
        'form': form,
    }
    return render(request, 'students/update.html', context)


def detail_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'students/detail.html', context)


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
