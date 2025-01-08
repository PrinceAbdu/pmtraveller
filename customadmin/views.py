from datetime import datetime as dt, timedelta, timezone
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from .models import Ride
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout
# from findingway.models import User 

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None and user.is_superuser:
#             login(request, user)
#             return redirect('view_admin_dashboard')
#         else:
#             return render(request, 'admin_login.html', {
#                 'error': 'Invalid credentials or insufficient permissions'
#             })
    
#     return render(request, 'admin_login.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from findingway.models import Ride

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {
                'error': 'Invalid credentials or insufficient permissions'
            })
    
    return render(request, 'admin_login.html')
# def view_admin_dashboard(request):
#    return render(request, 'admin_dashboard.html')


def view_admin_dashboard(request):
    # Get unique dates with rides, including status
    dates_with_rides = Ride.objects.values('time__date').distinct().order_by('-time__date')
    formatted_dates = [ride['time__date'] for ride in dates_with_rides]
    
    # Get rides for selected date
    selected_date = request.GET.get('date')
    rides = []
    
    if selected_date:
        rides = Ride.objects.filter(
            time__date=selected_date,
            status='SCHEDULED'
        ).order_by('time')
    
    return render(request, 'admin_dashboard.html', {
        'dates': formatted_dates,
        'rides': rides,
        'selected_date': selected_date
    })