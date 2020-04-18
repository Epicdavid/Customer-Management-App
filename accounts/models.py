from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=False)
    Phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registered = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    profile_pic = models.ImageField(default="signup.png",null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super().save(*args, **kwargs) # Call the real save() method    


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=False)

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    Category = models.CharField(max_length=200)
    Price = models.FloatField(max_length=200)
    Description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, related_name='tags',on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.name
       

class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, related_name='orders',on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,related_name='orders', on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=200, choices=STATUS)
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name


