from random import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import json
import os
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import never_cache, cache_page

from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def get_links_category():
   if settings.LOW_CACHE:
       key = 'links_category'
       links_category = cache.get(key)
       if links_category is None:
           links_category = ProductCategory.objects.filter(is_active=True)
           cache.set(key, links_category)
       return links_category
   else:
       return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
   if settings.LOW_CACHE:
       key = f'category_{pk}'
       category = cache.get(key)
       if category is None:
           category = get_object_or_404(ProductCategory, pk=pk)
           cache.set(key, category)
       return category
   else:
       return get_object_or_404(ProductCategory, pk=pk)


def get_links_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)

# def get_products_orederd_by_price():
#    if settings.LOW_CACHE:
#        key = 'products_orederd_by_price'
#        products = cache.get(key)
#        if products is None:
#            products = Product.objects.filter(is_active=True,
#                                   category__is_active=True).order_by('price')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(is_active=True,
#                                  category__is_active=True).order_by('price')
#
#
# def get_products_in_category_orederd_by_price(pk):
#    if settings.LOW_CACHE:
#        key = f'products_in_category_orederd_by_price_{pk}'
#        products = cache.get(key)
#        if products is None:
#            products = Product.objects.filter(category__pk=pk, is_active=True,
#                                              category__is_active=True).order_by('price')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(category__pk=pk, is_active=True,
#                               category__is_active=True).order_by('price')

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)

@cache_page(3600)
#@never_cache
def products(request, id_category=None, page=1):

    context = {
        'title': 'Geekshop | Каталог',
    }

    if id_category:
        products = Product.objects.filter(category_id=id_category).select_related('category')
    else:
        products = Product.objects.all().select_related('category')

    products = get_links_product()

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = get_links_product()
    # context['categories'] = ProductCategory.objects.all()
    context['categories'] = get_links_category()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/details.html'

def get_context_data(self, **kwargs):
    context = super(ProductDetail, self).get_context_data(**kwargs)
    context['product'] = get_product(self.kwargs.get("pk"))
    context['category'] = get_category(self.kwargs.get("pk"))
    return context