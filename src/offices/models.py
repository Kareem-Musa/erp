from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from locations.models import Region, Country, State

class Hquarter(models.Model):
    name = models.CharField(verbose_name=_('Hquarter Name'), max_length=200, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_hquarters', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                    related_name='region_countries', on_delete=models.CASCADE)
    state = models.ForeignKey(State, verbose_name=_('State'),
                                    related_name='state_hquarters', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Hquarters'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Sector(models.Model):
    name = models.CharField(verbose_name=_('Sector Name'), max_length=200, unique=True)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_('Hquarter'),
                                    related_name='hquarter_sectors', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Sectors'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Office(models.Model):
    name = models.CharField(verbose_name=_('Office Name'), max_length=200, unique=True)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_('Hquarter'),
                                    related_name='hquarter_offices', on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name=_('Sector'),
                                    related_name='sector_offices', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Offices'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Epoint(models.Model):
    name = models.CharField(verbose_name=_('Entry Point'), max_length=200, unique=True)
    Hquarter = models.ForeignKey(Hquarter, verbose_name=_('Hquarter'),
                                    related_name='hquarter_epoints', on_delete=models.CASCADE)
    Sector = models.ForeignKey(Sector, verbose_name=_('Sector'),
                                    related_name='sector_epoints', on_delete=models.CASCADE,  null=True, blank=True)
    office = models.ForeignKey(Office, verbose_name=_('Office'),
                                    related_name='office_epoints', on_delete=models.CASCADE,  null=True, blank=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Epoints'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Cpoint(models.Model):
    name = models.CharField(verbose_name=_('Collection Point'), max_length=200, unique=True)
    Hquarter = models.ForeignKey(Hquarter, verbose_name=_('Hquarter'),
                                    related_name='hquarter_cpoints', on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name=_('Sector'),
                                    related_name='sector_cpionts', on_delete=models.CASCADE, null=True, blank=True)
    office = models.ForeignKey(Office, verbose_name=_('Office'),
                                    related_name='office_cpoints', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Hquarters'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
