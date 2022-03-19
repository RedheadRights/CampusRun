from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

def index(request):

    return render(request, 'mapIntegration/index.html', {})

#def comment(request):

#    return HttpResponseRedirect(reverse('mapIntegration: index', kwargs={}))