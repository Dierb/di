from django.shortcuts import get_object_or_404, render
from . import models

# Create your views here.

def shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, 'shows_list.html', {'shows' : shows})

def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, 'shows_detail.html', {'show' : show})
