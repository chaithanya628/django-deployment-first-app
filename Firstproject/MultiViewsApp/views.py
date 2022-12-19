from django.shortcuts import render
from django.http import HttpResponse


# Create your views here...
def f1(request):
     return HttpResponse("<h2>Good Morning User ..! Have a nyc day </h2><hr/>");
     
def f2(request):
     return HttpResponse("<h6>Good afternoon User ..! Have a nyc day </h6><hr/>");
     
def f3(request):
     return HttpResponse("<h2>Good evening User ..! Have a nyc day </h2><hr/>");    