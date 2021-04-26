from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin

from .models import (
    Category, 
    Product, 
    Images, 
)


# Register your models here.
class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):
    lsit_display = ('name', 'paid', 'free',)
    ordering = ('name', )
    search_fields = ('name', 'paid', 'free',)

    fieldsets = (
        ('Категория', {
            "fields": (
                'name',
                'image',
            ),
        }),
    )

admin.site.register(Category, CategoryAdmin)

class ProductImageAdmin(AdminImageMixin, admin.TabularInline):
    model   = Images
    extra   = 1
    max_num = 4
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    
    list_display = ('category', 'name', 'price',  'discount', 'paid', 'free', 'downloaded', 'published_at', 'updated_at', )
    list_display_links = ('name',  'downloaded', 'published_at', 'updated_at', )
    search_fields = ('name', 'price', 'discount', 'category', 'downloaded', 'published_at', 'updated_at', )
    ordering = ('name', 'price', 'discount', 'paid', 'free', 'category',  'downloaded', 'published_at', 'updated_at', )
    list_editable = ('price', 'discount', 'paid', 'free',  'category', )

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = (
        ('Категория', {
            "fields": (
                ('category',)
            ),
        }),
        ('Файл модели', {
            "fields": (
                ('model_file',)
            ),
        }),
        ('Товар', {
            "fields": (
                ('name', 'slug', 'short_info', 'description', 'price', 'discount', 'paid', 'free', )
            ),
        }),
        ('Изображений', {
            "fields": (
                'image',
                # 'video_file',
                # 'video_link',
                'caption',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }
    
admin.site.register(Product, ProductAdmin)


