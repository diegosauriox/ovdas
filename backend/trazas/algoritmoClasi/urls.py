# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('algoritmosClasi/', views.index),
    path('createAlgoritmosClasi', views.create),
    path('deleteAlgoritmosClasi/<id>', views.destroy),
    path('updateAlgoritmosClasi/<int:id>', views.update)

]