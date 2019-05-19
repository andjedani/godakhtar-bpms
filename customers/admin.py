from django.contrib import admin
from customers.models import Customer, KeyPerson


class KeyPersonAdmin(admin.TabularInline):
    model = KeyPerson


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [KeyPersonAdmin, ]
    list_display = ("name", "customer_no", "priority", "section")
    list_filter = ("priority","section","classification","activity","ownership","deal_type")
    search_fields = ("name", "customer_no", "ceo", "section")
    fields = (("name", "customer_no", "priority"),
              ("financial_code", "national_id", "registration_no"),
              ("office_address", "site_address", "postal_code"),
              ("phone", "fax"), ("website", "email"),
              "ceo", ("ceo_office", "ceo_mobile", "ceo_email"),
              ("cfo", "cfo_office", "cfo_email"),
              ("logistic", "logistic_office", "logistic_email"),
              ("engineering", "engineering_office", "engineering_email"),
              ("expert", "expert_office", "expert_email"),
              ("maintenance_name", "maintenance_office", "maintenance_email"),
              ("section", "classification", "activity"),
              ("ownership", "owner"),
              "acquainted",
              ("deal_type", "deal_worth", "deal_history"),
              "mechanism",
              "deal_comments",
              "inquiry_history",
              ("last_godakhtar_visit", "last_customer_visit"),
              "comments")
