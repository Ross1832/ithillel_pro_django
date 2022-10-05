from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str
from django.db.models import Q

from .models import Groups
from .forms import GroupForm


@use_args({
    'name_group': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Groups.objects.all()

    if len(args) != 0 and args.get('name_group'):
        groups = groups.filter(Q(name_group=args.get('name_group', '')))

    context = {
        'title': 'List of Groups',
        'groups': groups,
    }
    return render(request, 'groups/list_of_group.html', context)


def create_group(request):
    if request.method == "GET":
        form = GroupForm()
    elif request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    group = get_object_or_404(Groups, pk=group_id)

    if request.method == "GET":
        form = GroupForm(instance=group)
    elif request.method == "POST":
        form = GroupForm(request.POST, instance=group)
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
