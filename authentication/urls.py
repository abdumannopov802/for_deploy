from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),

    path('check-username-email/', views.check_username_email, name='check_username_email'),
]

    