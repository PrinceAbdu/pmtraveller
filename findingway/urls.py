from django.contrib import admin
from django.urls import include, path
from . import views
# from traveller import findingway
# from traveller.findingway import views

urlpatterns = [
   
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.logout_view, name="signout"),
    path('logout', views.logout_view, name="signout"),
    path('signin_signup', views.signin_signup, name='signin_signup'),
    path('profile', views.profile, name='profile'),
    path('book-ride', views.book_ride, name='book-ride'),
    path('book_ride', views.book_ride, name='book-ride'),
    # path('/admin/dashboard/', views.admin_dashboard, n/ame='admin_dashboard'),
    path('get-available-slots/', views.get_available_slots, name='get_available_slots'),
    path('update-ride-status/', views.update_ride_status, name='update-ride-status'),
    # path('admin/login', views.signin_admin, name='book-ride')
]