from django.contrib import admin
from products.models import Attribute, AttributeChoices, Product


class AttributeChoicesTabular(admin.TabularInline):
    model = AttributeChoices


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeChoicesTabular, ]
    list_display = ("name", "type")
    list_filter = ("name", "type")
    search_fields = ("name",)

    model = Attribute


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_type", "product_class", "product_connection")
    list_filter = ("product_type", "product_class", "product_connection", "product_name")
    search_fields = ("product_type", "product_class", "product_connection")
    fields = ("product_name",
              ("product_type", "product_class"),
              ("product_size", "product_connection"), "available_attributes")
    readonly_fields = ("product_name",)
    model = Product
