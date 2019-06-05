from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^', views.ProductViewSet.as_view({'get': 'list'})),
    url(r'^types/', views.product_types, name='product-types'),
    url(r'^attributes/', views.AttributeViewSet.as_view({'get': 'list'}), name='attributes'),
    url(r'^(?P<product_id>[0-9])/attributes/?$',
        views.AttributeViewSet.as_view({'get': 'retrieve'}), name='get-product-attribute'),
]
