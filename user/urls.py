from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/', views.profile_user, name='profile'),
    path('profile/edit', views.edit_user, name='edit'),
]