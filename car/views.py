from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms
from django.contrib import messages
from .models import CarModel

# Create your views here.


class CarAddView(CreateView):
    model = CarModel
    form_class = forms.CarForm
    template_name = 'addcar.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request,'Car added succesfully')
        return super().form_valid(form)
    