# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views

from .viewss import volcanView

router = routers.DefaultRouter()
#router.register(r'trazas', views.TrazaViewSet)
#osrouter.register(r'volcanes', viewss.Test2)

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('volcanes2/', volcanView.index),
    #path('api/volcanesIdName/', volcanView.getIdName),
    #path('api/createVolcanes', volcanView.create),
    #path('api/deleteVolcan/<id>', volcanView.destroy),
    #path('api/updateVolcan/<int:id>', volcanView.update),
    #path('test/', views.test),
    #path('showzip/', viewss.download),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]