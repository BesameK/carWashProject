import datetime


from django.shortcuts import render
from .models import Order

# Create your views here.
def index(request):
    return render(request,"washers/index.html",{
        "orders":Order.objects.all()
    })
