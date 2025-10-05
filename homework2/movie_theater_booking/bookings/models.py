from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)  # e.g. "A1", "B5"
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('movie', 'seat_number')

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, related_name='bookings', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} booked {self.seat} at {self.booking_date}"