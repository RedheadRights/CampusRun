from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from addrToCoords import getGeoCoord

def index(request):
    return render(request, 'mapIntegration/index.html', {})

def submit(request):
    newRoute = route(routeName=request.POST['name'], addr1Lat=getGeoCoord(request.POST['addr1'])[0],\
        addr1Lng=getGeoCoord(request.POST['addr1'])[1], addr2Lat=getGeoCoord(request.POST['addr2'])[0],\
        addr2Lng=getGeoCoord(request.POST['addr2'])[1])    

    if(route.objects.filter(routeName=newRoute.routeName)):
        return HttpResponseRedirect(reverse('mapIntegration:run', kwargs={'routeName': newRoute.routeName}))
    else:
        newRoute.save()
        return HttpResponseRedirect(reverse('mapIntegration:run', kwargs={'routeName': newRoute.routeName}))

def run(request, routeName):
    currentRoute = get_object_or_404(route, routeName=routeName)
    routeLat1 = currentRoute.addr1Lat
    routeLng1 = currentRoute.addr1Lng
    routeLat2 = currentRoute.addr2Lat
    routeLng2 = currentRoute.addr2Lng
    return render(request, 'mapIntegration/run.html', {'routeLat1': routeLat1, 'routeLng1': routeLng1, 'routeLat2': routeLat2,\
         'routeLng2': routeLng2, 'routeName': routeName})

def submitRun(request, routeName):
    newRun = runData(path=get_object_or_404(route, routeName=routeName), name='jon', distance=7, time=request.POST['input_1'])
    newRun.save()
    return HttpResponseRedirect(reverse('mapIntegration:index', kwargs={}))