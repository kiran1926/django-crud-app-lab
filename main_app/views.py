from django.shortcuts import render
from .models import Plant


# Create your views here.
# controller code in python 
# we call these view functions
def home(request):
    #each view function takes a request object as an argument
    #request object contains metadata about the request
    return render(request, 'home.html')
    #HttpResponse is a class that takes a string as an argument
    #this is the response that will be sent to the client by returning it

def about(request):
    contact_info = 'You can reach support at support@plantcollector.com'
    return render(request, 'about.html', {
        'contact_info': contact_info
    })

# views.py


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants' : plants })

def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant' : plant })