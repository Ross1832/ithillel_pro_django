from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Groups
from .forms import GroupCreateForm, GroupUpdateForm, GroupFilterForm


def get_groups(request, ):
    groups = Groups.objects.all()
    filter_form = GroupFilterForm(data=request.GET, queryset=groups)
    context = {
        'title': 'List of Groups',
        'groups': groups,
        'filter_form': filter_form,
    }
    return render(request, 'groups/list_of_group.html', context)


def create_group(request):
    if request.method == "GET":
        form = GroupCreateForm()
    elif request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)

    if request.method == "GET":
        form = GroupUpdateForm(instance=group)
    elif request.method == "POST":
        form = GroupUpdateForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/update.html', {'form': form})


def detail_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    context = {
        'group': group
    }
    return render(request, 'groups/detail.html', context)


def delete_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)
    if request.method == "POST":
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'group': group})
