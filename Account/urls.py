from django.urls import path
from .import views

urlpatterns=[
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('reg',views.Register),
    path('userlogin',views.Login),
    path('userlogout',views.Logout,name='logout'),
    path('dashboard',views.Dasdboard,name='dashboard'),
]
