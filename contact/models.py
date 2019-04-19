from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CONTACT_TYPES = (
    (1, _("Customer")),
    (2, _("Office")),
    (3, _("Person"))
)


class Contact(models.Model):
    type = models.SmallIntegerField(verbose_name=_("Contact Type"), choices=CONTACT_TYPES)
