from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import (    
    Customer,
    Order,
    OrderItem,
    # ShippingAddress,
    OrderedItem,
)


# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)

class OrderedItemAdmin(admin.ModelAdmin):
    #  ('customer', 'product', 'product_amount', 'single_price', 'total_price', 'date_ordered', 'completed', )
    list_display       = ('customer', 'model', 'model_quantity', 'total_price', 'date_ordered', 'completed'  )
    list_display_links = ('customer', 'model', )
    # list_editable      = ('author', )
    ordering           = ('customer', 'model', 'model_quantity', 'single_price', 'total_price', 'date_ordered', 'completed',  )
    search_fields      = ('customer', 'model', 'model_quantity', 'single_price', 'total_price', 'date_ordered', 'completed', )

    fieldsets = (
        (
            'Клиент: ', {
                'fields':
                ('customer', 'model', 'model_quantity', 'single_price', 'total_price', 'completed', ),
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(OrderedItem, OrderedItemAdmin)