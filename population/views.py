from django.shortcuts import render, redirect
from .models import Population
from django.http import HttpResponse
import datetime
# Create your views here.
def cities(request):
    cities = Population.objects.all()
    print("''''''''''''''''''''''''''''''''''''''")
    print(type(cities))
    print("*************************************")
    data = []
    for city in cities:
        data += [city.city, city.admin_name, int(city.population)]
    print("''''''''''''''''''''''''''''''''''''''")
    print(type(data))
    now = datetime.datetime.now() 

    msg = f'Today is {now}'
    return render(request, 'landing.html', {"cities": cities})
    # return HttpResponse(msg, content_type='text/plain')

def delete_province(request, data_id):
    province = Population.objects.get(id=data_id)
    province.delete()
    print(data_id)
    return redirect('/population/')