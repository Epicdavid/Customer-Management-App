from django.shortcuts import render,redirect
from accounts.models import *
from accounts import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import *
from django.contrib.auth.models import Group


@login_required(login_url='login')
@admin_only
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





@unauthenticated_user
def register(request):
        form =  forms.UserForm()
        if request.method == 'POST':
            form = forms.UserForm(request.POST)
            if form.is_valid():          
                user = form.save()
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
                Customer.objects.create(user=user)

                return redirect('home')
            
        context = {
            'form':form
        }
        return render(request,'accounts/register.html',context)

@unauthenticated_user
def user_login(request):   
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,"Username or Password is Incorrect")  
        context = {}
        return render(request,'accounts/login.html',context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')    