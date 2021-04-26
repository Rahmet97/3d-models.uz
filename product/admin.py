from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
from .models import (
    Category,
    Product,
    Images,
)


@admin.register(Category)
class CategoryAdmin(AdminImageMixin, TranslationAdmin):
    lsit_display = ('name', 'paid', 'free',)
    ordering = ('name',)
    search_fields = ('name', 'paid', 'free',)

    fieldsets = (
        (_('Kategoriya'), {
            "fields": (
                'name',
                'image',
            ),
        }),
    )


# admin.site.register(CategoryAdmin)


class ProductImageAdmin(AdminImageMixin, admin.TabularInline):
    model = Images
    extra = 1
    max_num = 4


@admin.register(Product)
class ProductAdmin(AdminImageMixin, TranslationAdmin):
    inlines = [ProductImageAdmin]

    list_display = (
        'category', 'name', 'price', 'discount', 'paid', 'free', 'downloaded', 'published_at', 'updated_at',)
    list_display_links = ('name', 'downloaded', 'published_at', 'updated_at',)
    search_fields = ('name', 'price', 'discount', 'category', 'downloaded', 'published_at', 'updated_at',)
    ordering = ('name', 'price', 'discount', 'paid', 'free', 'category', 'downloaded', 'published_at', 'updated_at',)
    list_editable = ('price', 'discount', 'paid', 'free', 'category',)

    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (_('Kategoriya'), {
            "fields": (
                ('category',)
            ),
        }),
        (_('Model fayl'), {
            "fields": (
                ('model_file',)
            ),
        }),
        (_('Mahsulot'), {
            "fields": (
                ('name', 'slug', 'short_info', 'description', 'price', 'discount', 'paid', 'free',)
            ),
        }),
        (_('Rasm'), {
            "fields": (
                'image',
                # 'video_file',
                # 'video_link',
                'caption',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }


# admin.site.register(Product, ProductAdmin)
