from django.shortcuts import render
import razorpay
from django.conf import settings

# Create your views here.
# client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
client = razorpay.Client(
    auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))


def home(request):
    order_amount = 5000
    order_currency = 'INR'
    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id']
    context = {'amount': 500, 'api_key': settings.RAZORPAY_API_KEY,
               'order_id': payment_order_id}
    return render(request, 'base/index.html', context)
