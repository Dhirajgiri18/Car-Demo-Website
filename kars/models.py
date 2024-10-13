from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

def validate_year(value):
    if value > datetime.now().year:
        raise ValidationError(f'Year cannot be in the future: {value}')

class Car(models.Model):  # Changed Kar to Car for clarity
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(validators=[validate_year])  # Year validation
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        ordering = ['year']  # Orders cars by year by default

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
