from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id

            return redirect('payment:done',)
    else:
        form = OrderForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
