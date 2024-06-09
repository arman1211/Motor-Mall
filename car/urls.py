from django.urls import path
from . import views

urlpatterns = [
    path('addcar/', views.add_car, name='addcar'),
    
]