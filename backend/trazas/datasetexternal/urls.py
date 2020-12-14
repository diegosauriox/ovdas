# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()
#osrouter.register(r'estaciones', viewss.Test2)

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('loadVolcanesCSV', views.loadVolcanesCSV),
    path('loadIdentificacionSenal', views.loadIdentificacionSenalCSV),
    path('loadLocalizacionesCSV', views.loadLocalizacionesCSV)
]