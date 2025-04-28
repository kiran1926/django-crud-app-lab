from django.shortcuts import render
from django.http import HttpResponse


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

class Plant:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

# Create a list of Cat instances
plants = [
    Plant('Money Plant', 'Pilea peperomioides', 'Money Plant is a symbol of prosperity and good fortune.', 1),
    Plant('Snake Plant', 'Sansevieria trifasciata', 'Snake Plant is a symbol of prosperity and good fortune.', 2),
    Plant('Dumb Cane', 'Dracaena sp.', 'Dumb Cane is a symbol of prosperity and good fortune.', 3),
    Plant('Pothos', 'Epipremnum aureum', 'Pothos is a symbol of prosperity and good fortune.', 1)
]


def plants_index(request):
    return render(request, 'plants/index.html', { 'plants' : plants })

