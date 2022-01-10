from django.shortcuts import render
from . import models


# Create your views here.

def book(request):
    book = models.Book.objects.all()
    return render(request, 'index.html', {'book' : book})
