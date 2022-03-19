from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

def index(request):

    return render(request, 'mapIntegration/index.html', {})

def submit(request):
    newRun = route(routeName=request.POST['name'], addr1=request.POST['addr1'], addr2=request.POST['addr2'])
    newRun.save()
    return HttpResponseRedirect(reverse('mapIntegration:index', kwargs={}))