import datetime
from django.core.paginator import Paginator, EmptyPage
from .forms import CarForm, CreateUserForm
from django.shortcuts import render, redirect
from .models import Order, Car
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, "washers/home.html")


@login_required(login_url='login')
def cars(request):
    cars_items = Car.objects.all()
    p = Paginator(cars_items, 4)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        "cars": page,
    }
    return render(request, "washers/cars.html", context)


@login_required(login_url='login')
def index(request):
    return render(request, "washers/washer.html", {
        "orders": Order.objects.all()
    })


@login_required(login_url='login')
def createCar(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "washers/cars_form.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

    context = {'form': form, }
    return render(request, 'washers/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'washers/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
