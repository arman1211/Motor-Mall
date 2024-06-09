from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from car.models import CarModel,Purchase

# Create your views here.
bought_cars = []

def register_user(request):
    if request.method == 'POST':
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created successfully')
            return redirect('home')
    else:
        form = forms.RegisterUserForm()
    return render(request,'register.html',{'form': form})

def login_user(request):
    if request.method == 'POST':
        form = forms.LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in succesfull')
                return redirect('home')
            else:
                messages.warning(request,'Invalid username or password')
    else:
        form = forms.LoginUserForm()
    return render(request,'register.html',{'form': form ,'type': 'Login'})

def logout_user(request):
    logout(request)
    messages.success(request,'Logged out succesfull')
    return redirect('home')

def profile_user(request):
    purchases = Purchase.objects.filter(user = request.user)
    return render(request,'profile.html',{'purchases': purchases,})

def edit_user(request):
    form = forms.EditUserForm(instance = request.user)
    if request.method == 'POST':
        form = forms.EditUserForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'User updated successfully')
            return redirect('profile')
    return render(request,'register.html',{'form': form})

def buycar(request,id):
    car = CarModel.objects.get(pk=id)
    if car.quantity>0:
        car.quantity = car.quantity-1
        car.save()
        bought_cars.append(car)
        Purchase.objects.create(user = request.user, car = car)
        messages.success(request,f'Successfully Bought {car.name}')
        return redirect('profile')
    return render(request,'profile.html')
    