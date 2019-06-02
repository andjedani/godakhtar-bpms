from django.contrib import admin
from customers.models import Customer, KeyPerson, Branch, Personnel


class KeyPersonAdmin(admin.TabularInline):
    model = KeyPerson


class BranchAdmin(admin.TabularInline):
    model = Branch


class PersonnelAdmin(admin.TabularInline):
    model = Personnel


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [BranchAdmin, PersonnelAdmin, KeyPersonAdmin, ]
    list_display = ("name", "english_name", "customer_no", "priority",)
    list_filter = ("priority", "classification", "activity", "ownership")
    search_fields = ("name", "customer_no", "ceo")
    readonly_fields = ("customer_no", "verified")
    fields = (("name", "english_name", "customer_no"),
              ("financial_code", "national_id", "registration_no"),
              ("classification", "activity", "customer_size", "priority"),
              ("oil_section", "gas_section", "pertrochemical_section", "refinery_section", "plant_section"),
              ("ownership", "owner"),
              ("deal_type_gate", "deal_type_globe", "deal_type_check", "deal_type_ball", "deal_type_butterfly",
               "deal_type_repair_service", "deal_type_spare_parts", "deal_type_other", "deal_type_maintenance"),
              ("deal_worth", "deal_history"),
              "mechanism",
              "deal_comments",
              "inquiry_history",
              ("website", "email"),
              ("acquainted_expo", "acquainted_website", "acquainted_vendor", "acquainted_other",
               "acquainted_recommended"),
              ("last_godakhtar_visit", "last_customer_visit"),
              "comments", "verified")
