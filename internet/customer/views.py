from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from customer.models import Customer
from package.models import InternetPackage
from provider.models import Provider
import json


def register_customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        wallet = float(request.POST.get("wallet", 100000))

        customer = Customer.objects.create(name=name, phone=phone, wallet=wallet)
        customer.save()
        return HttpResponse(f"Customer {name} registered successfully!", status=201)


def buy_package(request, package_id):
    customer = Customer.objects.get(
        id=request.user.id
    )  
    package = InternetPackage.objects.get(id=package_id)

    if customer.wallet >= package.price:
        customer.wallet -= package.price
        customer.buyed_packages.add(package)
        customer.save()
        return HttpResponse(
            f"Package {package.name} purchased successfully!", status=200
        )
    else:
        return HttpResponse("Insufficient funds!", status=400)
    
    
def purchase_history(request):
    customer = Customer.objects.get(id=request.user.id)  
    purchases = customer.buyed_packages.all()
    purchase_data = [{"name": package.name, "price": package.price} for package in purchases]

   
    return JsonResponse(purchase_data, safe=False)

   
    with open('purchase_history.json', 'w') as json_file:
        json.dump(purchase_data, json_file)
    
    return HttpResponse("Purchase history exported successfully!", status=200)
