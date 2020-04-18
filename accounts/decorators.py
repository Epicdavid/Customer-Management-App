from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else: 
             return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles or request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                 return HttpResponse('Classified')      
        return wrapper_func
    return decorator           

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Customer':
            return redirect('accounts:user')
        if group == 'admin' or request.user.is_staff:
            return view_func(request, *args, **kwargs)

    return wrapper_function       
