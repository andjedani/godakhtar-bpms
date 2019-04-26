from django.contrib import admin
from contact.models import Contact, ContactDetail


# Register your models here.
class ContactDetailInline(admin.TabularInline):
    model = ContactDetail


@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailInline,
    ]


