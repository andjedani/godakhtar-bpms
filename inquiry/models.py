from django.db import models
from django.utils.translation import ugettext_lazy as _

from customers.models import Customer
from products.models import Product


class Inquiry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_('Customer'))
    qa_documents = models.CharField(max_length=127, blank=True, null=True, verbose_name=_('QA Documents'))
    guaranty = models.CharField(max_length=127, blank=True, null=True, verbose_name=_('Guaranty'))
    warranty = models.CharField(max_length=127, blank=True, null=True, verbose_name=_('Warranty'))
    packaging = models.CharField(max_length=5, blank=True, null=True, verbose_name=_('Packaging'))
    delivery_address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Delivery Address'))


class InquiryProducts(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='inquiry_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_inquiries')
    quantity = models.PositiveIntegerField(blank=False, null=False)
# PRODUCT_BODY_MATERIAL_CHOICES = (
#     ('WCB', _('WCB')), ('A105', _('A105')), ('SS304', _('SS304')), ('SS316', _('SS316')), ('CF8', _('CF8')),
#     ('CF3', _('CF3')), ('CF8M', _('CF8M')), ('CF3M', _('CF3M')), ('CF8C', _('CF8C')), ('LCB', _('LCB')),
#     ('LCC', _('LCC')), ('Al-Bronz', _('Al-Bronz')), ('WCC', _('WCC')), ('WC9', _('WC9')), ('WC6', _('WC6')),
#     ('C5', _('C5')), ('C12', _('C12')), ('Cast Iron', _('Cast Iron')), ('Inconel', _('Inconel')), ('Monel', _('Monel')),
#     ('Hatelloy', _('Hatelloy')), ('A351-CK3MCuN', _('A351-CK3MCuN')), ('A351-CD4MCu', _('A351-CD4MCu')),
#     ('A890-1A', _('A890-1A')), ('A890-4A', _('A890-4A'))
# )
#
# PRODUCT_TRIM_MATERIAL_CHOICES = (
#     ('WCB + ENP', _('WCB + ENP')), ('A105 + ENP', _('A105 + ENP')), ('LF2+ENP', _('LF2+ENP')),
#     ('SS316+TC', _('SS316+TC')),
#     ('SS316', _('SS316')), ('410', _('410')),
#     ('OT1', _('Overlay Trim No. #1')), ('OT2', _('Overlay Trim No. #2')),
#     ('OT3', _('Overlay Trim No. #3')), ('OT4', _('Overlay Trim No. #4')),
#     ('OT5', _('Overlay Trim No. #5')), ('OT5A', _('Overlay Trim No. #5A')),
#     ('OT6', _('Overlay Trim No. #6')), ('OT7', _('Overlay Trim No. #7')),
#     ('OT8', _('Overlay Trim No. #8')), ('OT8A', _('Overlay Trim No. #8A')),
#     ('OT9', _('Overlay Trim No. #9')), ('OT10', _('Overlay Trim No. #10')),
#     ('OT11', _('Overlay Trim No. #11')), ('OT12', _('Overlay Trim No. #12')),
#     ('OT13', _('Overlay Trim No. #13')), ('OT14', _('Overlay Trim No. #14')),
#     ('OT15', _('Overlay Trim No. #15')), ('OT16', _('Overlay Trim No. #16')),
#     ('OT17', _('Overlay Trim No. #17')), ('OT18', _('Overlay Trim No. #18')),
# )


# DESCRIPTION_TYPE_CHOICES = (
#     ('s', _('Single Choice')),
#     ('m', _('Multiple Choices')),
#     ('n', _('Numeric')),
# )
#

# class DescriptionType(models.Model):
#     name = models.CharField(max_length=64)
#     type = models.CharField(max_length=1, choices=DESCRIPTION_TYPE_CHOICES)
#     allowed_values = fields.ArrayField(models.CharField(max_length=127, null=False, blank=False), null=True, blank=True)
