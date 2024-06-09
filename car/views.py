from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages

# Create your views here.

def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Car added successfully')
            return redirect('home')
    else:
        form = forms.CarForm()
    return render(request,'addcar.html',{'form': form})