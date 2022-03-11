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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api2/', include('apibackend.urls')),
    path('api/', include('estaciones.urls')),
    path('api/', include('datasetexternal.urls')),
    path('api/', include('algoritmoClasi.urls')),
    path('api/', include('algoritmoDetec.urls')),
    path('api/', include('algoritmoPick.urls')),
    path('api/', include('avistamientoRegistro.urls')),
    path('api/', include('eventoLocali.urls')),
    path('api/', include('eventoMacro.urls')),
    path('api/', include('identificacion.urls')),
    path('api/', include('volcan.urls')),
    path('api/', include('waves.urls')),
    path('api/', include('alertas.urls')),
    path('api/', include('criterioAlerta.urls')),
    path('api/', include('paramDiscrFisc.urls')),
    path('api/', include('algoritmos.urls')),
    path('api/', include('paramContinuo.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
