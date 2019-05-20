from django.contrib import admin
from products.models import Description, DescriptionValues, Product, ProductType


class DescriptionValuesInline(admin.TabularInline):
    model = DescriptionValues


class ProductTypeDescriptionAdmin(admin.TabularInline):
    model = ProductType.descriptions.through


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductTypeDescriptionAdmin, ]
    model = ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_type", "product_size", "product_class", "product_connection")
    list_filter = ("product_type", "product_size", "product_class", "product_connection")
    search_fields = ("product_type", "product_size", "product_class", "product_connection")
    fields = (("product_type", "product_size", "product_class", "product_connection"),
              ("body_material", "trim_material", "operation"),)


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    inlines = [DescriptionValuesInline, ProductTypeDescriptionAdmin]
    model = Description
