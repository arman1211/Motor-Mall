from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from car.models import CarModel,Purchase
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView,View
from django.urls import reverse_lazy

# Create your views here.


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

class RegisterUserView(FormView):
    template_name = 'register.html'
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'User created successfully')
        return super().form_valid(form)

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
    return render(request,'register.html',{'form': form })

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect(reverse_lazy('home'))

@login_required
def profile_user(request):
    purchases = Purchase.objects.filter(user = request.user)
    return render(request,'profile.html',{'purchases': purchases,})

@login_required
def edit_user(request):
    form = forms.EditUserForm(instance = request.user)
    if request.method == 'POST':
        form = forms.EditUserForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'User updated successfully')
            return redirect('profile')
    return render(request,'register.html',{'form': form})

@login_required
def buycar(request,id):
    car = CarModel.objects.get(pk=id)
    if car.quantity>0:
        car.quantity = car.quantity-1
        car.save()
        Purchase.objects.create(user = request.user, car = car)
        messages.success(request,f'Successfully Bought {car.name}')
        return redirect('cardetails',id=id)
    else:
        messages.warning(request,f'Out of stock')
        return redirect('profile')
    