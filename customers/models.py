from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField

ACQUAINTED_CHOICES = (('A', 'Abbas'), ('B', 'Bagher'))

CUSTOMER_PRIORITY_CHOICES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
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
    ('1', _('1')),
    ('2', _('2'))
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
    website = models.CharField(max_length=120)
    # companyEmail
    email = models.CharField(max_length=120)
    # ceo
    ceo = models.CharField(max_length=120)
    # ceoOfficePhone
    ceo_office = models.CharField(max_length=20)
    # ceoCellPhone
    ceo_mobile = models.CharField(max_length=20)
    # ceoEmail
    ceo_email = models.CharField(max_length=120)
    cfo = models.CharField(max_length=120)
    cfo_office = models.CharField(max_length=20)
    cfo_mobile = models.CharField(max_length=20)
    cfo_email = models.CharField(max_length=120)
    logistic = models.CharField(max_length=120)
    logistic_office = models.CharField(max_length=20)
    logistic_mobile = models.CharField(max_length=20)
    logistic_email = models.CharField(max_length=120)
    engineering = models.CharField(max_length=120)
    engineering_office = models.CharField(max_length=20)
    engineering_mobile = models.CharField(max_length=20)
    engineering_email = models.CharField(max_length=120)
    expert = models.CharField(max_length=120)
    expert_office = models.CharField(max_length=20)
    expert_mobile = models.CharField(max_length=20)
    expert_email = models.CharField(max_length=120)
    maintenance_name = models.CharField(max_length=120)
    maintenance_office = models.CharField(max_length=20)
    maintenance_mobile = models.CharField(max_length=20)
    maintenance_email = models.CharField(max_length=120)
    key_persons = ArrayField(models.CharField(max_length=100, blank=True), blank=True, null=True)
    section = models.CharField(max_length=1, choices=CUSTOMER_SECTION_CHOICES)
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES)
    owner = models.CharField(max_length=100)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    classification = models.CharField(max_length=1, choices=CUSTOMER_CLASS_CHOICES)
    acquainted = models.CharField(max_length=1,choices=ACQUAINTED_CHOICES)
    deal_type = models.CharField(max_length=100)
    deal_worth = models.CharField(max_length=100)
    deal_history = models.BooleanField()
    inquiry_history = models.BooleanField()
    deal_comments = models.TextField()
    last_godakhtar_visit = models.DateField()
    last_visit_from_site = models.DateField()
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