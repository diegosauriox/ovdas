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
    path('estaciones/', views.index),
    path('createEstacion', views.create),
    path('deleteEstacion/<id>', views.destroy),
    path('updateEstacion/<int:id>', views.update),

]