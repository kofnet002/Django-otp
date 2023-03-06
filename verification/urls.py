from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage, name='register'),
    path('home', views.homePage, name='home'),
    path('otp/<str:uid>/', views.otpVerify, name='otp')
]
