from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader

# Create your views here.

from .models import Addresses


def base(request):
    theme = 'light'
    addresses = Addresses.objects.filter().order_by('id')
    data = serializers.serialize("python", Addresses.objects.all())
    return render(request, 'mainApp/datatable.html', {'addresses': addresses, 'theme': theme, 'data': data})

