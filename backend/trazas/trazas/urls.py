"""trazas URL Configuration

The `urlpatterns` list routes URLs to viewss. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function viewss
    1. Add an import:  from my_app import viewss
    2. Add a URL to urlpatterns:  path('', viewss.home, name='home')
Class-based viewss
    1. Add an import:  from other_app.viewss import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apibackend.urls')),
    path('api/', include('estaciones.urls')),
]
