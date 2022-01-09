# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'trazas', views.TrazaViewSet)
#osrouter.register(r'volcanes', viewss.Test2)

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('excecuteLoca/', views.excecuteLoca),
    path('executeAlgoAlejandro/', views.executeAlgoAlejandro),
    path('executeAlgorithms/', views.executeAgoritmos)

]