from django.shortcuts import render,redirect
from car.models import CarModel, CommentModel
from car.forms import CommentForm
from django.contrib import messages
from brand.models import BrandModel



def home(request,brand_name = None):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    if brand_name is not None:
        brands2 = BrandModel.objects.get(name= brand_name)
        cars = CarModel.objects.filter(brand = brands2)
    return render(request,'home.html',{'cars': cars, 'brands': brands})

def cardetails(request,id):
    car = CarModel.objects.get(pk=id)
    comments = CommentModel.objects.filter(car=car)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('cardetails', id=id)
    else:
        form = CommentForm()
    return render(request,'cardetails.html',{'car': car,'form': form ,'comments': comments})

def addcomment(request,id):
    if request.method == 'Post':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            car = CarModel.objects.get(pk=id)
            comment.car = car
            comment.user = request.user
            
            form.save()
            return redirect('cardetails',id=id)
