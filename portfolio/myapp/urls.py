from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name = 'home'),
    path('portfolio/',views.portfolio, name = 'portfolio')

]
