from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_type", "product_class", "product_connection")
    list_filter = ("product_type", "product_class", "product_connection")
    search_fields = ("product_type", "product_class", "product_connection")
    fields = (("product_type", "product_class"),
              "operation", )

    model = Product
