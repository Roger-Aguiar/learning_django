""" 
Name:         Roger Silva Santos Aguiar
Function:     This file creates the urls for the project
Initial date: October 8, 2020
Last update:  October 8, 2020 
"""

from django.urls import path
from . import views

urlpatterns = [path('', views.index, name = 'index'),]