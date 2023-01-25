from . import views
from django.urls import path
app_name = 'task4app'

urlpatterns = [
    path('', views.ind, name='index'),
    path('about/', views.about, name='about')
]