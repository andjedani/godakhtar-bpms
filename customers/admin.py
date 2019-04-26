from django.contrib import admin
from customers.models import Customer, Personnel


# Register your models here.
class PersonnelInline(admin.TabularInline):
    model = Personnel


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        PersonnelInline,
    ]
