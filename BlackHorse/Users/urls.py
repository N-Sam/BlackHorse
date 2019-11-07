from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home_page'),
    path('Users/register', views.register, name = 'register_page')

]