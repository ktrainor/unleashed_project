from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    output = ", ".join(tag.name for tag in tag_list)
    return HttpResponse(output)

