from django.forms.formsets import formset_factory
from django.shortcuts import render
from apps.city.models import City, Slider
from apps.page.forms import TicketForm, CalculatorForm

__author__ = 'alexy'

def home_view(request):
    form = TicketForm()
    city_list = City.objects.all().order_by('order')
    CalcFormSet = formset_factory(CalculatorForm, extra=3)
    slider = Slider.objects.all()
    return render(request, 'index.html', {
        'form': form,
        'slider_list': slider,
        'calc_formset': CalcFormSet,
        'all_city': city_list,
        'index': True
    })


def city_view(request, slug):
    form = TicketForm()
    city = City.objects.get(slug=slug)
    slider = city.slider_set.all()
    city_slider = city.cityslider_set.all()
    city_list = City.objects.all().order_by('order')
    return render(request, 'index.html', {
        'slug': slug,
        'city': city,
        'slider_list': slider,
        'city_slider_list': city_slider,
        'form': form,
        'all_city': city_list,
    })
