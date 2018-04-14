from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Produkt


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Produkt.objects.filter(dostępność=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Produkt.objects.filter(kategoria=category)

    context = {'kategoria': category,'kategorie': categories,'produkty': products,}

    return render(request, 'shop_app/product/list.html', context)


def product_detail(request, id, slug):
    produkt = get_object_or_404(Produkt, id=id, slug=slug, dostępność=True)
    context = { 'produkt': produkt }
    return render(request, 'shop_app/product/detail.html', context)