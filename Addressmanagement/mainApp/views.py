from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from .models import Addresses


def base(request):
    theme = 'light'
    addresses = Addresses.objects.filter().order_by('id')
    return render(request, 'mainApp/datatable.html', {'addresses': addresses, 'theme': theme})

