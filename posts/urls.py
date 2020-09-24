from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base_layout', views.base_layout, name='base_layout'),
    path('getdata', views.getdata, name='getdata'),
]