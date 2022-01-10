from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models

def hello_world(request):
    return HttpResponse('hello world')

def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post' : post})