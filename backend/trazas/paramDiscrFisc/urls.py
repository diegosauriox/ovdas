# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('indexpara/', views.index),
    #path('parametros/', views.recorrerParametros),
    path('createCriterio', views.create),
    path('deleteCriterio/<id>', views.destroy),
    path('updateCriterio/<id>', views.update),
    path('getMaxDr', views.getMaxDr)

]