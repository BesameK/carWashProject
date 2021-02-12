import datetime
from  django.core.paginator import Paginator, EmptyPage
from  .forms import CarForm
from django.shortcuts import render, redirect
from .models import Order,Car

# Create your views here.
def home(request):
    return render(request,"washers/home.html")

def cars(request):
    cars_items=Car.objects.all()
    p=Paginator(cars_items,4)
    page_num= request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)


    context={
        "cars": page,
    }
    return render(request,"washers/cars.html", context)

def index(request):

    return render(request,"washers/washer.html",{
        "orders":Order.objects.all()
    })
def createCar(request):
    form=CarForm()
    if request.method=="POST":
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return  render(request,"washers/cars_form.html",context)