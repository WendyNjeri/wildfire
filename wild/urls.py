from django.urls import path

from . import views

app_name = 'wild'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<event_id>[0-9]+)/', views.details, name='details'),



]