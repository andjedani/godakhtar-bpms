from django.contrib import admin
from customers.models import Customer, KeyPerson


class KeyPersonAdmin(admin.TabularInline):
    model = KeyPerson


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [KeyPersonAdmin, ]
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
              ("office_address", "site_address", "postal_code"),
              ("phone", "fax"), ("website", "email"),
              "ceo", ("ceo_office", "ceo_mobile", "ceo_email"),
              ("cfo", "cfo_office", "cfo_email"),
              ("logistic", "logistic_office", "logistic_email"),
              ("engineering", "engineering_office", "engineering_email"),
              ("expert", "expert_office", "expert_email"),
              ("maintenance_name", "maintenance_office", "maintenance_email"),
              ("acquainted_expo", "acquainted_website", "acquainted_vendor", "acquainted_other",
               "acquainted_recommended"),
              ("last_godakhtar_visit", "last_customer_visit"),
              "comments", "verified")
