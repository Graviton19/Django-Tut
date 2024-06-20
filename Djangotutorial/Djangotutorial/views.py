from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world!")

def about(request):
    return HttpResponse("About page!")

def contact(request):
    return HttpResponse("Contact page!")