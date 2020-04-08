from django.shortcuts import render, redirect
from .models import *
from . import forms
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})



@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def profile(request):
    orders = request.user.customer.orders.all()
    orders_c = orders.filter(status='Delivered').count()
    orders_p = orders.filter(status='Pending').count()
    total_o = orders.count()
    context={
        'orders':orders,
        'total_o': total_o,
        'delivered': orders_c,
        'pending': orders_p
        }
    return render(request, 'accounts/profile.html', context)

def account_setting(request):
    user = request.user.customer
    form = forms.CustomerForm(instance=user)
    if request.method == 'POST':
        form = forms.CustomerForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:edit')

    context={
        'form':form
    }
    return render(request, 'accounts/edit.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders.all()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {
        'customer':customer,
        'orders': orders,
        'myfilter': myfilter
    }
    return render(request, 'accounts/customer.html', context)  



@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def order(request,pk):
    order_formset = inlineformset_factory(Customer,Order, fields=('product','status'), extra=7)
    customer = Customer.objects.get(pk=pk)
    formset = order_formset(instance=customer)
    #form = forms.OrderForm() 
    if request.method == 'POST':
        #form = forms.OrderForm(request.POST)
        formset = order_formset(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('') 
        else:
            formset = order_formset(instance=customer)        
    context = {
        'formset':formset
    }
    return render(request, 'accounts/order_form.html', context)      


@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def update_order(request,pk):
    order = Order.objects.get(pk=pk)
    form = forms.OrderForm(instance=order)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('') 
        else:
            form = forms.OrderForm(instance=order)           
    context = {
        'form':form
    }
    return render(request, 'accounts/order_form.html', context)     


@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('') 
    context = {
        'item': order
    }    
    return render(request, 'accounts/delete_order.html', context)