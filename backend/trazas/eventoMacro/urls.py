# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('eventosMacro/', views.index),
    path('createEventoMacro', views.create),
    path('showEventoMacro/<id>', views.show),
    path('deleteEventoMacro/<id>', views.destroy),
    path('updateEventoMacro/<id>', views.update)

]