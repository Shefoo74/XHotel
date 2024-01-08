# payments/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('make_payment/', index, name='make_payment'),
    # Add other URLs as needed
]
