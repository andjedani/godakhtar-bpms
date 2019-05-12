from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

INQUIRY_HISTORY_CHOICES = (
    ('N', _('No Inquiry')),
    ('D', _('Has Deal')),
    ('R', _('Reject'))
)

DEAL_TYPE_CHOICES = (
    ('T', _('Gate')),
    ('G', _('Globe')),
    ('C', _('Check')),
    ('O', _('Ball')),
    ('B', _('Butterfly')),
    ('R', _('Repair Service')),
    ('M', _('Maintenance Service')),
    ('S', _('Spare Parts')),
    ('H', _('Other'))
)

ACQUAINTED_CHOICES = (
    ('E', _('Expo')),
    ('W', _('Website')),
    ('R', _('Recommended By Customers')),
    ('V', _('Vendor List')),
    ('H', _('Other'))
)

CUSTOMER_PRIORITY_CHOICES = (
    ('H', _('High')),
    ('M', _('Medium')),
    ('L', _('Low'))
)

CUSTOMER_SECTION_CHOICES = (
    ('O', _('Oil')),
    ('G', _('Gas')),
    ('P', _('Pertrochemical')),
    ('R', _('Refinery')),
    ('E', _('Plant')),
    ('C', _('Construction')),
    ('S', _('Steel')),
    ('H', _('Other'))
)

OWNERSHIP_CHOICES = (
    ('P', _('Private')),
    ('G', _('Government')),
    ('S', _('Semi-Private')),
    ('H', _('Other'))
)

ACTIVITY_CHOICES = (
    ('O', _('Operator')),
    ('C', _('Contractor')),
    ('S', _('Consultant')),
    ('H', _('Other'))
)

CUSTOMER_CLASS_CHOICES = (
    ('G', _('GC')),
    ('E', _('EPC')),
    ('F', _('Finance')),
    ('O', _('Operator')),
    ('S', _('Store')),
    ('H', _('Other'))

)

PERSONNEL_LOCATION_CHOICES = (
    ('O', _('Office')),
    ('C', _('Central Office')),
    ('S', _('Site')),
    ('H', _('Other'))
)
PERSONNEL_TYPE_CHOICES = (
    ('C', _('CEO')),
    ('F', _('CFO')),
    ('T', _('CTO')),
    ('E', _('Engineering Manager')),
    ('M', _('Maintenance Manager')),
    ('S', _('Expert')),
    ('H', _('Other'))
)

ACQUAINTED_CHOICES


class Customer(models.Model):
    # customerName
    name = models.CharField(max_length=200, verbose_name=_('Customer Name'))
    # customerNumber
    customer_no = models.CharField(max_length=30)
    # customerPriority
    priority = models.CharField(max_length=1, choices=CUSTOMER_PRIORITY_CHOICES)
    # financialCode
    financial_code = models.CharField(verbose_name=_('Economical Number'), max_length=20)
    # nationalId
    national_id = models.CharField(max_length=20)
    #  companyCode
    registration_no = models.CharField(max_length=20)
    # officeAddress
    office_address = models.CharField(max_length=255)

    site_address = models.CharField(max_length=255)
    # postalCode
    postal_code = models.CharField(max_length=20)
    # officeFax
    phone = models.CharField(max_length=20)
    # officePhone
    fax = models.CharField(max_length=20)
    # website
    website = models.CharField(max_length=127)
    # companyEmail
    email = models.CharField(max_length=127)
    # ceo
    ceo = models.CharField(max_length=127)
    # ceoOfficePhone
    ceo_office = models.CharField(max_length=20)
    # ceoCellPhone
    ceo_mobile = models.CharField(max_length=20)
    # ceoEmail
    ceo_email = models.CharField(max_length=127)
    cfo = models.CharField(max_length=127)
    cfo_office = models.CharField(max_length=20)
    cfo_email = models.CharField(max_length=127)
    logistic = models.CharField(max_length=127)
    logistic_office = models.CharField(max_length=20)
    logistic_email = models.CharField(max_length=127)
    engineering = models.CharField(max_length=127)
    engineering_office = models.CharField(max_length=20)
    engineering_email = models.CharField(max_length=120)
    expert = models.CharField(max_length=120)
    expert_office = models.CharField(max_length=20)
    expert_email = models.CharField(max_length=120)
    maintenance_name = models.CharField(max_length=120)
    maintenance_office = models.CharField(max_length=20)
    maintenance_email = models.CharField(max_length=120)
    key_persons = ArrayField(models.CharField(max_length=100, blank=True), blank=True, null=True)
    section = models.CharField(max_length=1, choices=CUSTOMER_SECTION_CHOICES)
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES)
    owner = models.CharField(max_length=100)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    classification = models.CharField(max_length=1, choices=CUSTOMER_CLASS_CHOICES)
    acquainted = models.CharField(max_length=1, choices=ACQUAINTED_CHOICES)
    deal_type = models.CharField(max_length=1, choices=DEAL_TYPE_CHOICES)
    deal_worth = models.CharField(max_length=100)
    deal_history = models.BooleanField()
    deal_comments = models.TextField()
    inquiry_history = models.CharField(max_length=1, choices=INQUIRY_HISTORY_CHOICES)
    last_godakhtar_visit = models.DateField()
    last_customer_visit = models.DateField()
    mechanism = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name

    #
# class Personnel(models.Model):
#     customer = models.ForeignKey(to='Customer', related_name='Customer', on_delete=models.CASCADE)
#     location = models.CharField(max_length=1, choices=PERSONNEL_LOCATION_CHOICES)
#     name = models.CharField(max_length=200, blank=False)
#     title = models.CharField(max_length=200, blank=False)
#     key_person = models.BooleanField()
#     contact = models.ForeignKey(to='contact.Contact', related_name='person_contact', on_delete=models.CASCADE)
#
#     def __str__(self):
#         s = self.name+ '(' + self.title + '@' + self.get_location_display() + ':' + self.customer.name + ')'
#         if self.key_person:
#             s += '(KEY)'
#         return s
#
