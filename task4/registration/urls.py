from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.reg, name='registration'),
    path('login', views.log, name='login'),
    path('logout', views.logout, name='logout')
]