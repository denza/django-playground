from django.shortcuts import render
from .models import Osoba

def poosobama(request):
    svao = Osoba.objects.all()
    return render(request, "pitanja/index.html", {'svao' : svao})
# Create your views here.
