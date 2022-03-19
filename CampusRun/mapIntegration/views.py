from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from addrToCoords import getGeoCoord

def index(request):

    return render(request, 'mapIntegration/index.html', {})

def submit(request):
    newRun = route(routeName=request.POST['name'], addr1Lat=getGeoCoord(request.POST['addr1'])[0],\
        addr1Lng=getGeoCoord(request.POST['addr1'])[1], addr2Lat=getGeoCoord(request.POST['addr2'])[0],\
        addr2Lng=getGeoCoord(request.POST['addr2'])[1])
    newRun.save()
    return HttpResponseRedirect(reverse('mapIntegration:index', kwargs={}))