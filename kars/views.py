from django.shortcuts import render,redirect, get_object_or_404
from .models import Car  # Change from Kar to Car

# Home view to display the list of cars
def home(request):
    cars = Car.objects.all()  # Change from Kar to Car
    return render(request, 'home.html', {'cars': cars})

# Detail view to display a specific car's details
def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)  # Change from Kar to Car
    return render(request, 'car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        # Create a new Car object
        car = Car(
            make=request.POST['make'],
            model=request.POST['model'],
            year=request.POST['year'],
            price=request.POST['price'],
            description=request.POST['description'],
            image=request.FILES['image'],
        )
        car.save()
        return redirect('home')  # Redirect to the home page after adding
    return render(request, 'add_car.html')

# View for editing an existing car
def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car.make = request.POST['make']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.price = request.POST['price']
        car.description = request.POST['description']
        
        if 'image' in request.FILES:
            car.image = request.FILES['image']  # Update image only if a new one is provided
        
        car.save()
        return redirect('car_detail', car_id=car.id)  # Redirect to car detail page
    return render(request, 'edit_car.html', {'car': car})