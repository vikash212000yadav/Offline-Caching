from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Feed
import json


# Create your views here.
def index(request):
    template = 'posts/index.html'
    results = Feed.objects.all()
    context = {
        'results': results,
    }
    return render(request, template, context)


def base_layout(request):
    template = 'posts/base.html'
    return render(request, template)


def getdata(request):
    results = Feed.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)
