from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RegionForm
from .models import Region

class RegionCreateView(CreateView):
    form_class = RegionForm
    template_name = 'locations/add_region.html'
    context_object_name = 'region'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Region'
        context['header'] = 'Add Region'
        context['action'] = 'Add Region'
        return context
