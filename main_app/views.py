from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# controller code in python 
# we call these view functions
def home(request):
    #each view function takes a request object as an argument
    #request object contains metadata about the request
    return HttpResponse('<h1>hello world</h1>')
    #HttpResponse is a class that takes a string as an argument
    #this is the response that will be sent to the client by returning it

def about(request):
    contact_info = 'You can reach support at support@plantcollector.com'
    return render(request, 'about.html', {
        'contact_info': contact_info
    })

