from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

DEAL_HISTORY_CHOICES = (
    ('y', _('Yes')),
    ('n', _('No')),
    ('z', _('Zero'))
)
INQUIRY_HISTORY_CHOICES = (
    ('n', _('No Inquiry')),
    ('d', _('Has Deal')),
    ('r', _('Reject'))
)

DEAL_TYPE_CHOICES = (
    ('t', _('Gate')),
    ('g', _('Globe')),
    ('c', _('Check')),
    ('o', _('Ball')),
    ('b', _('Butterfly')),
    ('r', _('Repair Service')),
    ('m', _('Maintenance Service')),
    ('s', _('Spare Parts')),
    ('h', _('Other'))
)

ACQUAINTED_CHOICES = (
    ('e', _('Expo')),
    ('w', _('Website')),
    ('r', _('Recommended By Customers')),
    ('v', _('Vendor List')),
    ('h', _('Other'))
)

CUSTOMER_PRIORITY_CHOICES = (
    ('h', _('High')),
    ('m', _('Medium')),
    ('l', _('Low'))
)

CUSTOMER_SECTION_CHOICES = (
    ('o', _('Oil')),
    ('g', _('Gas')),
    ('p', _('Pertrochemical')),
    ('r', _('Refinery')),
    ('e', _('Plant')),
    ('c', _('Construction')),
    ('s', _('Steel')),
    ('h', _('Other'))
)

OWNERSHIP_CHOICES = (
    ('p', _('Private')),
    ('g', _('Government')),
    ('s', _('Semi-Private')),
    ('h', _('Other'))
)

ACTIVITY_CHOICES = (
    ('o', _('Operator')),
    ('c', _('Contractor')),
    ('s', _('Consultant')),
    ('h', _('Other'))
)

CUSTOMER_CLASS_CHOICES = (
    ('g', _('GC')),
    ('e', _('EPC')),
    ('f', _('Finance')),
    ('o', _('Operator')),
    ('s', _('Store')),
    ('h', _('Other'))

)

PERSONNEL_LOCATION_CHOICES = (
    ('o', _('Office')),
    ('c', _('Central Office')),
    ('s', _('Site')),
    ('h', _('Other'))
)
PERSONNEL_TYPE_CHOICES = (
    ('c', _('CEO')),
    ('f', _('CFO')),
    ('t', _('CTO')),
    ('e', _('Engineering Manager')),
    ('m', _('Maintenance Manager')),
    ('s', _('Expert')),
    ('h', _('Other'))
)


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Customer Name'))
    customer_no = models.CharField(max_length=30)
    priority = models.CharField(max_length=1, choices=CUSTOMER_PRIORITY_CHOICES, blank=True, null=True)
    financial_code = models.CharField(verbose_name=_('Economical Number'), max_length=20, null=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    registration_no = models.CharField(max_length=20, blank=True, null=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)
    site_address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    website = models.CharField(max_length=127, blank=True, null=True)
    email = models.CharField(max_length=127, blank=True, null=True)
    ceo = models.CharField(max_length=127, blank=True, null=True)
    ceo_office = models.CharField(max_length=20, blank=True, null=True)
    ceo_mobile = models.CharField(max_length=20, blank=True, null=True)
    ceo_email = models.CharField(max_length=127, blank=True, null=True)
    cfo = models.CharField(max_length=127, blank=True, null=True)
    cfo_office = models.CharField(max_length=20, blank=True, null=True)
    cfo_email = models.CharField(max_length=127, blank=True, null=True)
    logistic = models.CharField(max_length=127, blank=True, null=True)
    logistic_office = models.CharField(max_length=20, blank=True, null=True)
    logistic_email = models.CharField(max_length=127, blank=True, null=True)
    engineering = models.CharField(max_length=127, blank=True, null=True)
    engineering_office = models.CharField(max_length=20, blank=True, null=True)
    engineering_email = models.CharField(max_length=120, blank=True, null=True)
    expert = models.CharField(max_length=120, blank=True, null=True)
    expert_office = models.CharField(max_length=20, blank=True, null=True)
    expert_email = models.CharField(max_length=120, blank=True, null=True)
    maintenance_name = models.CharField(max_length=120, blank=True, null=True)
    maintenance_office = models.CharField(max_length=20, blank=True, null=True)
    maintenance_email = models.CharField(max_length=120, blank=True, null=True)
    key_persons = ArrayField(models.CharField(max_length=100, blank=True), blank=True, null=True)
    section = models.CharField(max_length=1, choices=CUSTOMER_SECTION_CHOICES, blank=True, null=True)
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES, blank=True, null=True)
    classification = models.CharField(max_length=1, choices=CUSTOMER_CLASS_CHOICES, blank=True, null=True)
    acquainted = models.CharField(max_length=1, choices=ACQUAINTED_CHOICES, blank=True, null=True)
    deal_type = models.CharField(max_length=1, choices=DEAL_TYPE_CHOICES, blank=True, null=True)
    deal_worth = models.CharField(max_length=127, blank=True, null=True)
    deal_history = models.CharField(max_length=1, choices=DEAL_HISTORY_CHOICES, blank=True, null=True)
    deal_comments = models.TextField(null=True)
    inquiry_history = models.CharField(max_length=1, choices=INQUIRY_HISTORY_CHOICES, blank=True, null=True)
    last_godakhtar_visit = models.CharField(max_length=127, blank=True, null=True)
    last_customer_visit = models.CharField(max_length=127, blank=True, null=True)
    mechanism = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return self.name
