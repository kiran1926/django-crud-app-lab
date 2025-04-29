from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Plant, Watering, Fertilizer
from .forms import WateringForm, FertilizerForm


# Create your views here.
# controller code in python 
# we call these view functions
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    contact_info = 'You can reach support at support@plantcollector.com'
    return render(request, 'about.html', {
        'contact_info': contact_info
    })

# views.py

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', { 'plants' : plants })

@login_required
def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    fertilizer_form = FertilizerForm()
    return render(request, 'plants/detail.html', { 
        'plant': plant,
        'watering_form': watering_form,
        'fertilizer_form': fertilizer_form
    })

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
        # Update the plant's last_watered date
        plant = Plant.objects.get(id=plant_id)
        plant.last_watered = new_watering.date
        plant.save()
    return redirect('plant-detail', plant_id=plant_id)

@login_required
def add_fertilizer(request, plant_id):
    form = FertilizerForm(request.POST)
    if form.is_valid():
        new_fertilizer = form.save(commit=False)
        new_fertilizer.plant_id = plant_id
        new_fertilizer.save()
    return redirect('plant-detail', plant_id=plant_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plants-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'species', 'description', 'age', 'light_requirements', 'water_frequency']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['species', 'description', 'age', 'light_requirements', 'water_frequency']

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'
