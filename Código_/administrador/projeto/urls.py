"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('arquitetura/', include('arquitetura.urls')),
    path('administrador/', include('administrador.urls')),
    path('moderador/', include('moderador.urls')),
    path('usuario/', include('usuario.urls')),
    path('psicologo/', include('psicologo.urls')),


    path('', RedirectView.as_view(url='/administrador/')),
    path('', RedirectView.as_view(url='/moderador/')),
    path('', RedirectView.as_view(url='/usuario/')),
    path('', RedirectView.as_view(url='/psicologo/')),



]

