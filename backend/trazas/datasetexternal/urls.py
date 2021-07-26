# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()
#router.register(r'subirArchivo', views.MyUploadView, basename='MyModel')
#osrouter.register(r'estaciones', viewss.Test2)

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('loadVolcanesCSV', views.loadVolcanesCSV),
    path('loadIdentificacionSenal', views.loadIdentificacionSenalCSV),
    path('loadLocalizacionesCSV', views.loadLocalizacionesCSV),
    path('loadRegistroCSV', views.loadRegistroCSV)

]