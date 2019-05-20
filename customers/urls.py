from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from customers import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]