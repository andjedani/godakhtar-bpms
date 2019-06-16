# Register your models here.
from django.contrib import admin

from inquiry.models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    model = Inquiry
