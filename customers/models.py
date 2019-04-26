from django.db import models
from contact.models import Contact
from django.utils.translation import ugettext_lazy as _

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


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    contact = models.ForeignKey(to='contact.Contact', related_name='customer_contact', on_delete=models.CASCADE)
    no = models.CharField(max_length=30)
    priority = models.CharField(max_length=1, choices=CUSTOMER_PRIORITY_CHOICES)
    eco_code = models.CharField(verbose_name=_('Economical Number'), max_length=20)
    section = models.CharField(max_length=1, choices=CUSTOMER_SECTION_CHOICES)
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES)
    owner = models.CharField(max_length=100)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    classification = models.CharField(max_length=1, choices=CUSTOMER_CLASS_CHOICES)
    channel = models.CharField(max_length=100)
    buy_type = models.CharField(max_length=100)
    previous_deal = models.BooleanField()
    sales_comments = models.TextField()
    last_godakhtar_visit = models.DateField()
    last_visit_from_site = models.DateField()
    mechanism = models.CharField(max_length=100)
    comments = models.TextField()
    
    def __str__(self):
        return self.name    


class Personnel(models.Model):
    customer = models.ForeignKey(to='Customer', related_name='Customer', on_delete=models.CASCADE)
    location = models.CharField(max_length=1, choices=PERSONNEL_LOCATION_CHOICES)
    name = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    key_person = models.BooleanField()
    contact = models.ForeignKey(to='contact.Contact', related_name='person_contact', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
