from django.conf.urls import url
from rest_framework import routers
from django.urls import include

from inquiry import views
router = routers.DefaultRouter()
router.register(r'', views.InquiryViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    # url(r'^', views.InquiryViewSet.as_view({'get': 'list'})),
    # TODO: Endpoint for list of customers : id, name, english_name, customer_no, section
]
