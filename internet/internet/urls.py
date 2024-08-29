from django.urls import path
from .views import register_provider, add_package, register_customer, list_packages, buy_package, purchase_history

urlpatterns = [
    path('register/provider/', register_provider, name='register_provider'),
    path('add/package/', add_package, name='add_package'),
    path('register/customer/', register_customer, name='register_customer'),
    path('packages/', list_packages, name='list_packages'),
    path('buy/package/<int:package_id>/', buy_package, name='buy_package'),
    path('purchase/history/', purchase_history, name='purchase_history'),
]
