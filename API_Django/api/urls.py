from django.contrib import admin
from django.urls import path,include
from . import views

app_name='api'

urlpatterns = [
    path('', views.api_view,name='api_list'),
    path('add/', views.api_add,name='add'),
]
