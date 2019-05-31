from django.db import models
from django.contrib.postgres import fields
from django.utils.translation import ugettext_lazy as _

PRODUCT_TYPE_CHOICES = (
    ('3WB', _('3 Way Ball Valve')), ('B', _('Ball Valve')), ('BGa', _('Bellowse Gate Valve')),
    ('BGl', _('Bellowse Globe Valve')), ('BF', _('Butterfly valve')), ('C', _('Check Valve')),
    ('CrB', _('Cryogenic Ball Valve')), ('CrBf', _('Cryogenic Butterfly Valve')),
    ('CrC', _('Cryogenic Check Valve')), ('CrGa', _('Cryogenic Gate Valve')),
    ('CrGl', _('Cryogenic Globe Valve')), ('Ga', _('Gate Valve')),
    ('Gl', _('Globe')), ('KG', _('Knife Gate Valve')),
    ('P', _('Plug Valve')), ('TCG', _('Through Conduit Gate Valve')),

)


PRODUCT_CLASS_CHOICES = (('125', _('125')), ('150', _('150')), ('200', _('200')),
                         ('250', _('250')), ('300', _('300')), ('400', _('400')), ('600', _('600')),
                         ('800', _('800')), ('900', _('900')), ('1500', _('1500')), ('2500', _('2500')),
                         ('3000', _('3000')), ('4500', _('4500')), ('5000', _('5000')), ('10000', _('10000')),
                         ('PN10', _('PN10')), ('PN16', _('PN16')), ('PN20', _('PN20')), ('PN50', _('PN50')),)

PRODUCT_CONNECTION_CHOICES = (
    ('Flange / RF', _('Flange / RF')), ('Flange / FF', _('Flange / FF')),
    ('Flange / RTJ', _('Flange / RTJ')), ('Flange / Large Femal', _('Flange / Large Femal')),
    ('Flange / Large Mal', _('Flange / Large Mal')), ('Grove Flange', _('Grove Flange')),
    ('Wafer / RF', _('Wafer / RF')), ('Wafer / FF', _('Wafer / FF')),
    ('Butt weld', _('Butt weld')), ('Socket Weld', _('Socket Weld')),
    ('Scrowed', _('Scrowed')), ('Threaded', _('Threaded')), ('Lug', _('Lug')),
    ('Semi Lug', _('Semi Lug')), ('SW / Thrd', _('SW / Thrd')))


PRODUCT_OPERATION_CHOICES = (
    ('GO', _('Gear Operated')), ('LO', _('Lever Operated')),
    ('EA', _('Electrical Actuator')), ('PA', _('Pnumatic Actuator')),
    ('GOOA', _('Gas Over Oil Actuator')), ('BS', _('Bare Shaft')),
    ('H', _('Handwheel')), ('EAM', _('Electrical Actuator with master station(MOV)')),
)


class Product(models.Model):
    product_type = models.CharField(max_length=9, choices=PRODUCT_TYPE_CHOICES)
    # product_size = models.CharField(max_length=9, choices=PRODUCT_SIZE_CHOICES, verbose_name=_('Size'))
    product_class = models.CharField(max_length=9, choices=PRODUCT_CLASS_CHOICES, verbose_name=_('Class'))
    product_connection = models.CharField(max_length=22, choices=PRODUCT_CONNECTION_CHOICES,
                                          verbose_name=_('Connection'))
    operation = models.CharField(max_length=9, choices=PRODUCT_OPERATION_CHOICES,
                                 verbose_name=_('Operation'))

    def __str__(self):
        return self.product_type
