from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from customers import views

urlpatterns = [
    url(r'^', views.CustomerViewSet.as_view({'get': 'list'})),
    url(r'^short/', views.CustomerShortListSet.as_view({'get': 'list'})),
    # TODO: Endpoint for list of customers : id, name, english_name, customer_no, section
]
