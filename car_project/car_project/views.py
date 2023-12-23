from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
# from car.models import Car,Brand

# def category(request, category_slug=None):
#     cars = Car.objects.all()
#     brands = Brand.objects.all()
#     print(category_slug)
#     if category_slug is not None:
#         # brands = Brand.objects.get(brand_name=category_slug)
#         cars = Car.objects.filter(brand__brand_name=category_slug)
#         brand=Brand.objects.get(brand_name=category_slug)
#         cars=Car.objects.filter(brand=brand)
#     return render(request, 'home.html', {'cars': cars, 'brands': brands})

# def home(request):
#     return render(request,'home.html')
    



