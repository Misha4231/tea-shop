from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\nYou have successfully places an order.Your order ID is {order.id}'
    send_mail(subject,message,'pysmtpsender8@gmail.com',[order.email])
    return True