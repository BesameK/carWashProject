from django.urls import path
from . import  views

urlpatterns= [
    path("",views.index,name="index"),
    # path("oneWeek",views.oneWeek,name="oneWeek")
]