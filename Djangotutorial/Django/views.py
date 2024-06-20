from django.shortcuts import render

# Create your views here.
def all_django(request):
    return render(request,'Django/all_django.html')