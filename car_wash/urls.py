from django.urls import path
from . import  views

urlpatterns= [
    path("",views.index,name="index"),
    path("cars/",views.cars,name="cars"),
    path("createCar/",views.createCar,name="createCar"),
]