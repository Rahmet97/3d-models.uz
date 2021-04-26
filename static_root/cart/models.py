from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

from product.models import Product, Category


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,  on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.user)

    # @property
    # def get_ordered_total(self):
    #     ordereditems = self.customer_orders.all()
    #     total = sum([item.get_total for item in ordereditems if item.completed == False])
    #     return total 

    # @property
    # def get_ordered_items(self):
    #     ordereditems = self.customer_orders.all()
    #     total = sum([item.product_amount for item in ordereditems if item.completed == False])
    #     return total

    # @property
    # def get_completed_total(self):
    #     ordereditems = self.customer_orders.all()
    #     total = sum([item.get_total for item in ordereditems if item.completed == True])
    #     return total 

    # @property
    # def get_completed_items(self):
    #     ordereditems = self.customer_orders.all()
    #     total = sum([item.product_amount for item in ordereditems if item.completed == True])
    #     return total

        

def post_save_user_receiver(sender, instance, created, **kwargs):
    user = instance
    if created:
        customer = Customer(user=user)
        customer.save()

post_save.connect(post_save_user_receiver, sender=User)


class OrderedItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name="customer_orders", verbose_name = "Customer")
    model    = models.CharField(max_length=300, blank=True, null=True, verbose_name="Model")
    image    = models.ImageField(upload_to="ordered-product/%Y/%m/%d/", blank=True, null=True, verbose_name='Image')
    model_quantity = models.IntegerField(default=0, verbose_name="Model Quantity")
    single_price   = models.FloatField(default=0, verbose_name="Price")
    total_price    = models.FloatField(default=0, verbose_name="Total Price")
    date_ordered   = models.DateTimeField(auto_now_add=True, verbose_name = "Ordered Date")
    completed      = models.BooleanField(default=False, verbose_name="Completed")

    def __str__(self):
        return str(self.customer) + " | " + str(self.completed)
    
   

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ["-date_ordered"]
        verbose_name = "Ordered Models"
        verbose_name_plural = "Ordered Models"

def post_save_customer_receiver(sender, instance, created, **kwargs):
    customer = instance
    if created:
        ordered_item = OrderedItem(customer=customer)
        ordered_item.save()

post_save.connect(post_save_customer_receiver, sender=Customer)



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) # Customer returns user email
    complete = models.BooleanField(default=False, verbose_name='Completed')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    # transaction_id = models.CharField(max_length=100, null=True, verbose_name='Translation Id')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    model = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name="ordered_product", null=True, verbose_name="Model")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name="Order")
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Quantity")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
    cart_field = models.BooleanField(default=False) # This field is only changed through checkbox in cart page

    class Meta:
        verbose_name="Order Model"
        verbose_name_plural="Order Models"

    @property
    def get_total(self):
        price = 0
        if self.model.discount:
            price = self.model.discount
        else:
            price = self.model.price
        total = price * self.quantity
        return total


class OrderSingleItem(models.Model):
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_single_item')
    model     = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False) # after download is completed this field value must be changed to True
