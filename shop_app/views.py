from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, Produkt
from cart.forms import CartAddProductForm
from cart.cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Produkt.objects.filter(dostępność=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Produkt.objects.filter(kategoria=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
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
