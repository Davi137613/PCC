from django.shortcuts import render

def pagprincipal(request):
    return render(request, 'arquitetura/pagprincipal.html')

def base(request):
    return render(request, 'templates/base.html')

