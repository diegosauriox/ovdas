# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('identificacion/', views.index),
    path('createIdentificacion', views.create),
    path('deleteIdentificacion/<id>', views.destroy),
    path('updateIdentificacion/<id>', views.update),
    path('identificacionFilter', views.filter),

]