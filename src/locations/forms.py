from django import forms
from .models import Region, Country, State, Locality, Unity, City

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control py-1'})
