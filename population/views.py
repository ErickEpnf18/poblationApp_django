from contextlib import nullcontext
from queue import Empty
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Population
from django.http import HttpResponse
import datetime
# Create your views here.
def cities(request):
    cities = Population.objects.all()
    return render(request, 'landing.html', {"cities": cities})

def delete_province(request, data_id):
    province = Population.objects.get(id=data_id)
    province.delete()
    print(data_id)
    return redirect('/')

def searchbar(request):
    nameOfCity= ''
    
    if request.method == 'POST':
        search = request.POST.get('searchbar')
        nameOfCity = Population.objects.all().filter(city=search)
    # now = datetime.datetime.now() 
    # msg = f'Today is {now} and {nameOfCity.values_list()} and your type {search}'
    # return redirect('/', {"searchData": nameOfCity})
    # return HttpResponse(msg, content_type='text/plain')
    return render(request, 'landing.html', {"searchData": nameOfCity})
    
    