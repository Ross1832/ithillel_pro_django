from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
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
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f"""
    CREATE FORM
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>
    """
    return HttpResponse(html_form)


def update_group(request, group_id):
    group = Groups.objects.get(pk=group_id)

    if request.method == "GET":
        form = GroupForm(instance=group)
    elif request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f"""
    CREATE FORM
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>
    """
    return HttpResponse(html_form)


def detail_group(request, group_id):
    group = Groups.objects.get(pk=group_id)
    context = {
        'group': group
    }
    return render(request, 'groups/detail.html', context)


