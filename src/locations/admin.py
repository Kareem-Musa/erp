from django.contrib import admin
from .models import Region, Country, State, Locality, Unity, City

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Locality)
admin.site.register(Unity)
admin.site.register(City)
