from django.db import models
from django.utils.translation import ugettext_lazy as _
from tools import utils

DEAL_HISTORY_CHOICES = (
    ('y', _('Yes')),
    ('n', _('No')),
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
    ('s', _('Spare Parts')),
    ('h', _('Other')),
    ('m', _('Maintenance Service')),
)

ACQUAINTED_CHOICES = (
    ('e', _('Expo')),
    ('w', _('Website')),
    ('v', _('Vendor List')),
    ('r', _('Recommended By Customers')),
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
    ('e', _('End User')),
    ('c', _('Contractor')),
    ('s', _('Consultant')),
    ('h', _('Other'))
)

CUSTOMER_CLASS_CHOICES = (
    ('g', _('GC')),
    ('e', _('EPC')),
    ('f', _('Trader')),
    ('o', _('End User')),
    ('s', _('Store')),
    ('h', _('Other'))

)

CUSTOMER_SIZE_CHOICES = (
    ('s', _("Small")),
    ('m', _("Medium")),
    ('l', _("Large")),
)


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Customer Name'), unique=True)
    english_name = models.CharField(max_length=200, verbose_name=_('English Name'), unique=True)
    customer_no = models.CharField(verbose_name=_('Customer Number'), max_length=30, null=True, blank=True, unique=True)
    priority = models.CharField(verbose_name=_('Priority'), max_length=1, choices=CUSTOMER_PRIORITY_CHOICES, blank=True,
                                null=True)
    financial_code = models.CharField(verbose_name=_('Economical Number'), max_length=20, null=True, blank=True,
                                      unique=True)
    national_id = models.CharField(verbose_name=_('National ID'), max_length=20, blank=True, null=True, unique=True)
    registration_no = models.CharField(verbose_name=_('Registration Number'), max_length=20, blank=True, null=True)
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=20, blank=True, null=True, unique=True)
    website = models.URLField(verbose_name=_('Website address'), max_length=127, blank=True, null=True)
    email = models.EmailField(verbose_name=_('email address'), max_length=127, blank=True, null=True)
    customer_size = models.CharField(max_length=1, choices=CUSTOMER_SIZE_CHOICES, blank=False, null=False)
    oil_section = models.BooleanField(default=False, verbose_name=_('Oil'))
    gas_section = models.BooleanField(default=False, verbose_name=_('Gas'))
    pertrochemical_section = models.BooleanField(default=False, verbose_name=_('Pertrochemical'))
    refinery_section = models.BooleanField(default=False, verbose_name=_('Refinery'))
    plant_section = models.BooleanField(default=False, verbose_name=_('Plant'))
    construction_section = models.BooleanField(default=False, verbose_name=_('Construction'))
    steel_section = models.BooleanField(default=False, verbose_name=_('Steel'))
    other_section = models.BooleanField(default=False, verbose_name=_('Other'))
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES, blank=True, null=True)
    classification = models.CharField(max_length=1, choices=CUSTOMER_CLASS_CHOICES, blank=False, null=False)
    acquainted_expo = models.BooleanField(default=False, verbose_name=_('Expo'))
    acquainted_website = models.BooleanField(default=False, verbose_name=_('Website'))
    acquainted_vendor = models.BooleanField(default=False, verbose_name=_('Vendor List'))
    acquainted_other = models.BooleanField(default=False, verbose_name=_('Other'))
    acquainted_recommended = models.BooleanField(default=False, verbose_name=_('Recommended By Customers'))
    deal_type_gate = models.BooleanField(default=False, verbose_name=_('Gate'))
    deal_type_globe = models.BooleanField(default=False, verbose_name=_('Globe'))
    deal_type_check = models.BooleanField(default=False, verbose_name=_('Check'))
    deal_type_ball = models.BooleanField(default=False, verbose_name=_('Ball'))
    deal_type_butterfly = models.BooleanField(default=False, verbose_name=_('Butterfly'))
    deal_type_repair_service = models.BooleanField(default=False, verbose_name=_('Repair Service'))
    deal_type_spare_parts = models.BooleanField(default=False, verbose_name=_('Spare Parts'))
    deal_type_other = models.BooleanField(default=False, verbose_name=_('Other'))
    deal_type_maintenance = models.BooleanField(default=False, verbose_name=_('Maintenance Service'))
    deal_worth = models.CharField(max_length=127, blank=True, null=True)
    deal_history = models.CharField(max_length=1, choices=DEAL_HISTORY_CHOICES, blank=True, null=True)
    deal_comments = models.TextField(null=True, blank=True)
    inquiry_history = models.CharField(max_length=1, choices=INQUIRY_HISTORY_CHOICES, blank=True, null=True)
    last_godakhtar_visit = models.CharField(max_length=127, blank=True, null=True)
    last_customer_visit = models.CharField(max_length=127, blank=True, null=True)
    mechanism = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.email = utils.clean_up_lower(self.email)
        self.website = utils.clean_up_lower(self.website)
        self.name = utils.clean_up(self.name)
        self.english_name = utils.clean_up(self.english_name)
        self.owner = utils.clean_up(self.owner)
        self.deal_comments = utils.clean_up(self.deal_comments)
        self.comments = utils.clean_up(self.comments)
        self.national_id = utils.clean_up_alpha_numeric(self.national_id)
        self.postal_code = utils.clean_up_alpha_numeric(self.postal_code)
        self.registration_no = utils.clean_up_alpha_numeric(self.registration_no)
        self.financial_code = utils.clean_up_alpha_numeric(self.financial_code)

        if not self.pk:
            customer_no_draft = self.classification + self.customer_size
            same_customers = Customer.objects.filter(classification=self.classification,
                                                     customer_size=self.customer_size).order_by('-customer_no')
            serial = 1
            if same_customers:
                serial = int(same_customers[0].customer_no[2:]) + 1

            customer_no_draft = customer_no_draft.upper() + f'{serial:3}'.replace(' ', '0')
            self.customer_no = customer_no_draft

        super().save()

    def __str__(self):
        return self.name


PERSONNEL_TYPE_CHOICES = (
    ('c', _('CEO')),
    ('f', _('CFO')),
    ('t', _('CTO')),
    ('e', _('Engineering Manager')),
    ('m', _('Maintenance Manager')),
    ('s', _('Expert')),
    ('h', _('Other'))
)


class Personnel(models.Model):
    name = models.CharField(max_length=127, blank=False)
    role = models.CharField(max_length=2, choices=PERSONNEL_TYPE_CHOICES, blank=False)
    office_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=127, blank=True, null=True)
    comments = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='personnel')

    def save(self, *args, **kwargs):
        self.email = self.email.lower().strip()
        if self.email == "":
            self.email = None
        super().save()


class KeyPerson(models.Model):
    name = models.CharField(max_length=127, blank=False)
    office = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=127, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='key_persons')

    def save(self, *args, **kwargs):
        self.email = self.email.lower().strip()
        if self.email == "":
            self.email = None
        super().save()


BRANCH_TYPE_CHOICES = (
    ('c', _("Headquarters")),
    ('o', _("Office")),
    ('s', _("Site")),
    ('h', _("Other"))
)


class Branch(models.Model):
    name = models.CharField(max_length=127, blank=False)
    type = models.CharField(max_length=1, choices=BRANCH_TYPE_CHOICES)
    address = models.CharField(verbose_name=_('Address'), max_length=255, blank=True, null=True)
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=20, blank=True, null=True, unique=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20, blank=True, null=True)
    fax = models.CharField(verbose_name=_('Fax Number'), max_length=20, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='branchs')

