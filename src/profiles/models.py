from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import User
from locations.models import Region, Country, State, Locality, Unity, City
from offices.models import Hquarter, Sector, Office

class Profile(models.Model):
    class DGREES(models.TextChoices):
        PROFESSOR = 'PROF', _('professor')
        DECTOR = 'DR', _('dector')
        MASTER = 'MR', _('master')
        BACHELOR = 'BC', _('bachelor')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/', null=True, blank=True)
    bio = models.TextField(verbose_name=_('Bio'), null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                related_name='region_profiles', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                related_name='country_profiles', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_('State'),
                                related_name='state_profiles', on_delete=models.CASCADE, null=True, blank=True)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_('Hquarter'),
                                related_name='hquarter_profiles', on_delete=models.CASCADE, null=True, blank=True)
    sector = models.ForeignKey(Sector, verbose_name=_('Sector'),
                                related_name='sector_profiles', on_delete=models.CASCADE, null=True, blank=True)
    office = models.ForeignKey(Office, verbose_name=_('Office'),
                                related_name='office_profiles', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_dean = models.BooleanField(default=False)
    head_section = models.BooleanField(default=False)
    sub_hedad_section = models.BooleanField(default=False)
    super_teacher = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)
    tutor = models.BooleanField(default=False)
    dgree = models.CharField(verbose_name='Dgree', max_length=4, choices=DGREES.choices)
    finan = models.BooleanField(default=False)
    auditor = models.BooleanField(default=False)
    accountant = models.BooleanField(default=False)
    registerer = models.BooleanField(default=False)

    class Meta:
        #ordering = ['created']
        verbose_name_plural = 'Prfoiles'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        pass
