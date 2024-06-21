from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.
def all_django(request):
    chais = ChaiVarity.objects.all()
    return render(request,'Django/all_django.html',{'chais':chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk= chai_id)
    return render(request,'Django/chai_detail.html',{'chai':chai})