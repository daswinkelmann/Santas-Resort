from django.db import models


# Create your models here.
class Amenity(models.Model):
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon representing the amenity. "
        "Use a font-awesome class eg. 'fa fa-wifi'"
        )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('family', 'Family'),
    ]

    ROOM_STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
    ]

    number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=ROOM_STATUS_CHOICES)
    amenities = models.ManyToManyField(Amenity, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.number} ({self.type})"

    class Meta:
        ordering = ['number']
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Service(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('maintenance', 'Maintenance'),
    ]

    CATEGORY_CHOICES = [
        ('accommodation', 'Accommodation'),
        ('spa', 'Spa & Wellness'),
        ('transportation', 'Transportation'),
        ('food', 'Food & Beverage'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    max_capacity = models.PositiveIntegerField(
        help_text="Maximum number of users that can use"
        "the service simultaneously."
        )
    duration = models.DurationField(
        help_text="Typical duration for which the service is used."
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(
        max_length=255,
        help_text="Physical location where the service is provided."
        )

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
