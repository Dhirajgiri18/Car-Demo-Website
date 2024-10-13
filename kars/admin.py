from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price')  # Fields to display in the list view
    search_fields = ('make', 'model')  # Enable search functionality
    list_filter = ('year',)  # Add filter options

admin.site.register(Car, CarAdmin)
