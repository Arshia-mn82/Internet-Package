from package.models import InternetPackage
from django.http.response import HttpResponse,JsonResponse
def list_packages(request):
    packages = InternetPackage.objects.all()
    package_list = ''.join([f"<li>{package.name} - {package.price} - {package.providers.name}</li>" for package in packages])
    
    return HttpResponse(f"<ul>{package_list}</ul>")
    