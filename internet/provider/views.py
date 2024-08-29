from provider.models import Provider
from package.models import InternetPackage
from django.http.response import HttpResponse
import json

def register_provider(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        provider = Provider.objects.create(name=name, verification=False)
        provider.save()
        return HttpResponse(f"Provider {name} registered successfully!", status=201)
    
    
def add_package(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        provider_id = int(request.POST.get('provider_id'))
        provider = Provider.objects.get(id=provider_id)
        
        package = InternetPackage.objects.create(name=name, price=price, providers=provider)
        package.save()
        return HttpResponse(f"Package {name} added successfully!", status=201)

    