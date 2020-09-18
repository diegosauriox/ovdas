# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('algoritmosDetect/', views.index),
    path('createAlgoritmosDetect', views.create),
    path('deleteAlgoritmosDetect/<id>', views.destroy),
    path('updateAlgoritmosDetect/<int:id>', views.update)

]