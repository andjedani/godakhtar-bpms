from django.conf.urls import url
from rest_framework import routers
from django.urls import include

from inquiry import views
router = routers.DefaultRouter()
router.register(r'', views.InquiryViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^(?P<inquiry_id>[0-9]+)/addproduct/?$',
        views.add_product_to_inquiry, name='add-product-to-inquiry'),
    url(r'^(?P<inquiry_id>[0-9]+)/deleteproduct/?$',
        views.delete_product_from_inquiry, name='delete-product-from-inquiry'),
    # TODO: Endpoint for list of customers : id, name, english_name, customer_no, section
]
