from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from products import views

product_attributes = views.AttributeViewSet.as_view({'get': 'retrieve'})
product_by_name = views.ProductViewSet.as_view({'get': 'retrieve'})
router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)
router.register(r'attributes', views.AttributeViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^list/(?P<product_name>[A-Za-z0-9]+)/?$',
        product_by_name, name='get-product-by-name'),
    url(r'^(?P<product_id>[0-9])/attributes/?$',
        product_attributes, name='get-product-attribute'),
    url(r'^types/', views.product_types, name='get-product-types'),
]
