from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError


class Attribute(models.Model):
    ATTRIBUTE_TYPE_CHOICES = (
        ('n', _('Numeric')),
        ('c', _('Choices')),
        ('t', _('Text'))
    )
    name = models.CharField(max_length=63, null=False, blank=False, verbose_name=_('Attribute Name'))
    type = models.CharField(max_length=1, choices=ATTRIBUTE_TYPE_CHOICES, null=False, blank=False,
                            verbose_name=_('Attribute Choices'))
    validator = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Validator'))

    def __str__(self):
        return self.name


class AttributeChoices(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_choices')
    value = models.CharField(max_length=63, null=False, blank=False, verbose_name=_('Attribute Value'))


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('BV', _('Ball Valve')),
        ('GV', _('Bellowse Gate Valve')),
        ('GLV', _('Bellowse Globe Valve')),
        ('BUV', _('Butterfly valve')),
        ('CV', _('Check Valve')),
        ('CryoBV', _('Cryogenic Ball Valve')),
        ('CryoBUV', _('Cryogenic Butterfly Valve')),
        ('CryoBUV', _('Cryogenic Butterfly Valve')),
        ('CryoCV', _('Cryogenic Check Valve')),
        ('CryoGV', _('Cryogenic Gate Valve')),
        ('CryoGLV', _('Cryogenic Globe Valve')),
        ('GV', _('Gate Valve')),
        ('GLV', _('Globe')),
        ('KFGV', _('Knife Gate Valve')),
        ('PV', _('Plug Valve')),
        ('TCGV', _('Through Conduit Gate Valve')),
    )

    PRODUCT_CLASS_CHOICES = (('125', _('125')), ('150', _('150')), ('200', _('200')),
                             ('250', _('250')), ('300', _('300')), ('400', _('400')), ('600', _('600')),
                             ('800', _('800')), ('900', _('900')), ('1500', _('1500')), ('2500', _('2500')),
                             ('3000', _('3000')), ('4500', _('4500')), ('5000', _('5000')), ('10000', _('10000')),
                             ('PN10', _('PN10')), ('PN16', _('PN16')), ('PN20', _('PN20')), ('PN50', _('PN50')),)

    PRODUCT_CONNECTION_CHOICES = (
        ('Fe', _('Flange')),
        ('WF', _('Wafer')),
        ('BW', _('Butt weld')),
        ('SW', _('Socket Weld')),
        ('SE', _('Scrowed')),
        ('TH', _('Threaded')),
        ('LUG', _('Lug')),)

    PRODUCT_SIZE_CHOICES = (('1/4', _('1/4')), ('1/2', _('1/2')), ('3/4', _('3/4')), ('1', _('1')),
                            ('1 1/2', _('1 1/2')), ('2', _('2')), ('2 1/2', _('2 1/2')), ('3', _('3')),
                            ('4', _('4')), ('5', _('5')), ('6', _('6')), ('8', _('8')),
                            ('10', _('10')), ('12', _('12')), ('14', _('14')), ('16', _('16')),
                            ('18', _('18')), ('20', _('20')), ('22', _('22')), ('24', _('24')),
                            ('26', _('26')), ('28', _('28')), ('30', _('30')), ('32', _('32')),
                            ('34', _('34')), ('36', _('36')), ('38', _('38')), ('40', _('40')),
                            ('42', _('42')), ('44', _('44')), ('46', _('46')), ('48', _('48')),
                            ('50', _('50')), ('52', _('52')), ('54', _('54')), ('56', _('56')),
                            ('58', _('58')), ('60', _('60')), ('62', _('62')), ('64', _('64')),
                            ('66', _('66')), ('68', _('68')), ('70', _('70')), ('72', _('72')),
                            ('74', _('74')), ('76', _('76')), ('78', _('78')), ('80', _('80')),
                            ('82', _('82')), ('84', _('84')), ('86', _('86')), ('88', _('88')),
                            ('90', _('90')), ('92', _('92')), ('94', _('94')), ('96', _('96')),
                            ('98', _('98')), ('100', _('100')),
                            )

    product_type = models.CharField(max_length=8, choices=PRODUCT_TYPE_CHOICES, null=False, blank=False,
                                    verbose_name=_('Product Type'))
    product_size = models.CharField(max_length=5, choices=PRODUCT_SIZE_CHOICES, null=False, blank=False,
                                    verbose_name=_('Product Size'))
    product_class = models.CharField(max_length=6, choices=PRODUCT_CLASS_CHOICES, verbose_name=_('Class'))
    product_connection = models.CharField(max_length=3, choices=PRODUCT_CONNECTION_CHOICES,
                                          verbose_name=_('Connection'))
    available_attributes = models.ManyToManyField(Attribute, verbose_name=_('Available Attributes'),
                                                  related_name='product')

    class Meta:
        unique_together = ('product_type', 'product_class', 'product_connection', 'product_size')

    @property
    def product_name(self):
        return ''.join([self.product_type, self.product_class, self.product_connection, self.product_size])

    def __str__(self):
        return self.product_name

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if not self.pk:
    #         same_products = len(Product.objects.filter(product_type=self.product_type,
    #                                                    product_connection=self.product_connection,
    #                                                    product_class=self.product_class,
    #                                                    product_size=self.product_size))
    #         if same_products > 0:
    #             raise ValidationError("Product Already Exists")
    #         
    #         super().save()
