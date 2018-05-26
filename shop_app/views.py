from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Produkt
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.db.models import Sum
from django.db.models import Count


def product_list(request, category_slug=None):
    category = None
    sum = {}
    key = 0;
    categories = Category.objects.all()
    products = Produkt.objects.filter(dostępność=True)
    products2 = Produkt.objects.filter(dostępność=True)
    sum_total = Produkt.objects.aggregate(Count('nazwa')).get('nazwa__count',0.00)
    for c in categories:
        products2 = Produkt.objects.filter(kategoria=c)
        key = products2.aggregate(Count('nazwa')).get('nazwa__count', 0.00)
        if key == None:
            key = 0;
        sum[c] = key
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Produkt.objects.filter(kategoria=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'sum_total' : sum_total,
        'sum' : sum
    }
    return render(request, 'shop_app/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Produkt, id=id, slug=slug, dostępność=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop_app/product/detail.html', context)
