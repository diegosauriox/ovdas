# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('localizaciones/', views.index),
    path('createLocalizacion', views.create),
    path('deleteLocalizacion/<id>', views.destroy),
    path('updateLocalizacion/<id>', views.update),
    path('lastItemMaxLocali/', views.loadLastItem)

]