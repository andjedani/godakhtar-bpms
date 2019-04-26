from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CONTACT_TYPES = (
    (1, _("Customer")),
    (2, _("Office")),
    (3, _("Person"))
)
CONTACT_DETAIL_CHOICES = (
    ('M', _('Mobile')),
    ('E', _('E-Mail')),
    ('A', _('Address')),
    ('P', _('Phone')),
    ('W', _('Work')),
    ('F', _('Fax')),
    ('S', _('Site')),
    ('O', _('Office')),
    ('C', _('Postal Code')),
    ('D', _('Office Address')),
    ('F', _('Site Address')),
    ('N', _('National Code')),
    ('H', _('Other')),
)


class Contact(models.Model):
    # type = models.SmallIntegerField(verbose_name=_("Contact Type"), choices=CONTACT_TYPES)
    pass


class ContactDetail(models.Model):
    label = models.CharField(max_length=1, choices=CONTACT_DETAIL_CHOICES)
    value = models.CharField(max_length=200)
    contact = models.ForeignKey(to="Contact", related_name='contact', on_delete=models.CASCADE)

    def __str__(self):
        return self.label + " : " + self.value
