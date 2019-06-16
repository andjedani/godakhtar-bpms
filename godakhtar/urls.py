from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

admin.site.site_header = 'GODAKHTAR'
admin.site.site_title = "GODAKHTAR"
admin.site.index_title = "GODAKHTAR"

urlpatterns = i18n_patterns(
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^beta-version/', admin.site.urls),
    url(r'^api/v0/customers/', include('customers.urls')),
    url(r'^api/v0/products/', include('products.urls')),
    url(r'^api/v0/inquiry/', include('inquiry.urls')),
)
