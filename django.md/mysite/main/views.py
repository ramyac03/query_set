from django.shortcuts import render

# Create your views here and template for that 
from django.http import HttpResponse
from .models import Define,Info

def index(response,id):
         x =Define.objects.get(id=id)
#          info =x.info_set.get(id =id)
#          return render(response,"main/base.html",{}) --->using base.html
         return render(response,"main/list.html",{"x":x}) #--->list.html


def v1(response):
          
         return HttpResponse("<h1>hello<h1>")

def home(response):
         return render(response,"main/home.html",{})
