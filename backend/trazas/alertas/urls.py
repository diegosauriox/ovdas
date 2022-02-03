# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('obtenerAlertas/', views.obtenerAlertas),
    path('guardarAlertas/',views.guardarAlertas),
    path('getAllAlertas/',views.getAllAlertas),
    path('alertaVT/',views.crearAlertaVT),

    
]