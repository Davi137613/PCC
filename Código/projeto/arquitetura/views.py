from django.shortcuts import render
from django.http import HttpResponse

def pagprincipal(request):
    return render(request, 'arquitetura/pagprincipal.html')

def base(request):
    return render(request, 'templates/base.html')

