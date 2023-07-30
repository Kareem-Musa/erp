from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    name = models.CharField(verbose_name=_('Region Name'), max_length=100, unique=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']
        verbose_name_plural = _('Regions')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Country(models.Model):
    name = models.CharField(verbose_name=_('Country Name'), max_length=100, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_countries', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class State(models.Model):
    name = models.CharField(verbose_name=_('State Name'), max_length=100, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_states', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                    related_name='country_states', on_delete=models.CASCADE, null=True, blank=-True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = _('States')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class Locality(models.Model):
    name = models.CharField(verbose_name=_('Locality Name'), max_length=100, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_localities', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                    related_name='country_localities', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_('State'),
                                    related_name='state_localities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = _('Localities')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

# unity model
class Unity(models.Model):
    name = models.CharField(verbose_name=_('Unity Name'), max_length=100, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_unities', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                    related_name='country_unities', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_('State'),
                                    related_name='state_unities', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name=_('Locality'),
                                    related_name='locality_unities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = _('Unities')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

class City(models.Model):
    name = models.CharField(verbose_name=_('Unity Name'), max_length=100, unique=True)
    region = models.ForeignKey(Region, verbose_name=_('Region'),
                                    related_name='region_cities', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),
                                    related_name='country_cities', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_('State'),
                                    related_name='state_cities', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name=_('Locality'),
                                    related_name='locality_cities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
