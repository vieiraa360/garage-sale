from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from checkout.models import Order


# Create your views here.

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    
    
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL ,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'GBP',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': order,
                                                    'form':form})
    