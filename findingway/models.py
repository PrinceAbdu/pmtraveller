from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime, timedelta

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Ride(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rides'
    )
    starting_location = models.CharField(max_length=255)
    ending_location = models.CharField(max_length=255)
    time = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=0)  # Duration in minutes
    distance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('SCHEDULED', 'Scheduled'),
            ('COMPLETED', 'Completed'),
            ('CANCELLED', 'Cancelled')
        ],
        default='SCHEDULED'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def end_time(self):
        return self.time + timedelta(minutes=self.duration)

    @classmethod
    def get_booked_slots(cls, date):
        # Get all rides for the given date
        day_start = datetime.combine(date, datetime.min.time())
        day_end = datetime.combine(date, datetime.max.time())
        
        rides = cls.objects.filter(
            time__date=date,
            status='SCHEDULED'
        )
        
        booked_slots = []
        for ride in rides:
            current_time = ride.time
            while current_time < ride.end_time:
                booked_slots.append(current_time.strftime('%H:%M'))
                current_time += timedelta(minutes=15)
                
        return booked_slots