from django.shortcuts import render,redirect
from car.models import CarModel
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
    print(car.quantity)
    return render(request,'cardetails.html',{'car': car})

