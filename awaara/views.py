from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):

    dests = Destination.objects.all()
    revs = Reviews.objects.all()
    return render(request, "index.html", {'dests': dests, 'revs': revs})
