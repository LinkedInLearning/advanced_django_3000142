from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Business
# Create your views here.

def business_listing(request):
    template = loader.get_template('business_listing.html')
    businesses = Business.objects.all()
    return HttpResponse(template.render({'businesses': businesses}, request))
