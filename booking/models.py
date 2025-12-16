from django.db import models
from core.models import Service


# Create your models here.
class Booking(models.Model):
    user_id = models.IntegerField(
        null=True, blank=True, help_text="ID of the user making the booking."
        )
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Booking for {self.full_name} - {self.service.name} "
            f"from {self.check_in} to {self.check_out}"
        )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
