from django.contrib import admin
from django.urls import include, path
from . import views
# from traveller import findingway
# from traveller.findingway import views

urlpatterns = [
   
    path('', views.admin_login, name="admin_login"),
    path('dashboard', views.view_admin_dashboard, name="admin_dashboard"),

]