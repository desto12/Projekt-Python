from decimal import Decimal
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def payment_process(request):
    order_id = request.session.get('order.id')
    order = get_object_or_404(Order, id=order_id)

    paypal_dict = {
        'business': 'bartix96pl@gmail.com',
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'cos',
        'invoice': str(order.id),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment:done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form,
               }
    return render(request, 'payment/process.html', context)
