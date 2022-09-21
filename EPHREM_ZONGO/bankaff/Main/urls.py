from django.contrib import admin
from django.urls import path
from Main import views as Main_views

urlpatterns = [
    path('admin/' , admin.site.urls),     
    path('', Main_views.home, name='home'),                 
    path('/contact', Main_views.contact, name='contact'),
    path('/agences', Main_views.agences, name='agences'),
    path('/clients', Main_views.clients, name='clients'),
    

]              