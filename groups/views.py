from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, DetailView, CreateView

from .models import Groups
from students.models import Student
from .forms import GroupCreateForm, GroupUpdateForm, GroupFilterForm


class ListGroupView(ListView):
    model = Groups
    template_name = 'groups/list_of_group.html'



class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Groups
    form_class = GroupCreateForm
    template_name = 'groups/create.html'
    success_url = reverse_lazy('groups:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()
        return response


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    model = Groups
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            initial['headman_field'] = 0

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        else:
            form.instance.headman = None
        form.save()

        return response


class DetailGroupView(LoginRequiredMixin, DetailView):
    model = Groups
    template_name = 'groups/detail.html'
    context_object_name = 'group'


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Groups
    template_name = 'groups/delete.html'
    success_url = reverse_lazy('groups:list')
