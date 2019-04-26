from django.contrib import admin
from customers.models import Customer, Personnel


# Register your models here.
class PersonnelInline(admin.TabularInline):
    model = Personnel


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'customer_no', 'eco_code'), ('priority', 'section', 'activity', 'classification'),
        ('owner', 'ownership'),
        ('channel', 'buy_type'), 'previous_deal', 'sales_comments', ('last_godakhtar_visit', 'last_visit_from_site'),
        'mechanism', 'comments','contact')
    inlines = [
        PersonnelInline,
    ]
