from django.urls import path

from . import views

app_name = 'wild'

urlpatterns = [
    path('', views.index, name='index'),

]