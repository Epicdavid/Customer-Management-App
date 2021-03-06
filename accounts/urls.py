from django.urls import path
from . import views


app_name='accounts'

urlpatterns=[
    path('products', views.products, name='products'),
    path('<int:pk>', views.customers, name='customer'),
    path('<int:pk>/order', views.order, name='order'),
    path('update/<pk><int:c_pk>', views.update_order, name='update'),
    path('delete/<pk><int:c_pk>', views.delete_order, name='delete'),
    path('profile', views.profile, name='user'),
    path('edit', views.account_setting, name='edit'),
    path('update/<pk>', views.updateCustomer, name='update_c')

    ]