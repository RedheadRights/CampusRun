from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('run/<str:routeName>', views.run, name='run'),
    path('submitRun/<str:routeName>', views.submitRun, name='submitRun'),
]