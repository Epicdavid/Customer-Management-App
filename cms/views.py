from django.shortcuts import render
from accounts.models import *

def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {
        'orders': orders,
        'products': products,
        'customers': customers,
        'total_o': total_orders,
        'total_c': total_customers,
        'pending': pending,
        'delivered': delivered,
    }
    return render(request,'accounts/dashboard.html', context)