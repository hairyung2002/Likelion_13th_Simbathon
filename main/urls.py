from django.urls import path
from .views import *
from . import views

app_name = "main"

urlpatterns = [
    path('', views.LoginPage, name="LoginPage"),
    path('MembershipPage/', views.MembershipPage, name="MembershipPage"),
    path('MyPage/', views.MyPage, name="MyPage"),
    path('Create_Member/', views.Create_Member, name="Create_Member"),
    path('Check_Member/', views.Check_Member, name='Check_Member'),
] 