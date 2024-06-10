from django.urls import path
from . import views

urlpatterns = [
    path('addcar/', views.CarAddView.as_view(), name='addcar'),
    
]