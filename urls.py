from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name = 'myfirstblogspot'),
    path('customers/', views.customers, name = 'customers'),
    path('packages/', views.packages, name = 'packages'),
]