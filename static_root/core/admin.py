from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin

from .models import (    
    AboutUs,
    VideoModel,
    PortFolio,
    Images,
    ArticleModel,
)


# Register your models here.
class AboutUsAdmin(admin.ModelAdmin):
    # ('title', 'image', 'video', 'description', 'pub_date', )
    list_display       = ('pk', 'title', 'image', 'video', 'pub_date', )
    list_display_links = ('pk', 'title', 'image', 'video', 'pub_date', )
    # list_editable      = ('author', )
    ordering           = ('title', 'image', 'video',  'pub_date', )
    search_fields      = ('title', 'image', 'video',  'pub_date', )

    fieldsets = (
        (
            'Contents: ', {
                'fields':
                ('title', 'image', 'video', 'description', ),
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(AboutUs, AboutUsAdmin)

class VideoModelAdmin(admin.ModelAdmin):
    # ('video_url', 'video_file', 'title', 'description', 'published_at', )
    list_display       = ('pk', 'title', 'published_at', )
    list_display_links = ('pk', 'title', 'published_at', )
    # list_editable      = ('author', )
    ordering           = ('pk', 'title', 'published_at', )
    search_fields      = ('pk', 'title', 'published_at', )

    fieldsets = (
        (
            'Contents: ', {
                'fields':
                ('title', 'video_url', 'video_file', 'description',),
            }
        ),
        
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(VideoModel, VideoModelAdmin)


class PortfolioImageAdmin(AdminImageMixin, admin.TabularInline):
    model   = Images
    extra   = 1
    max_num = 3
class PortfolioAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [PortfolioImageAdmin]
    
    # ('image', 'caption', 'name', 'slug', 'short_info', 'description', 'published_at', 'updated_at', )
    list_display = ('name', 'short_info', 'published_at', 'updated_at', )
    list_display_links = ('name', 'short_info', 'published_at', 'updated_at', )
    search_fields = ('name', 'short_info', 'published_at', 'updated_at', )
    ordering = ('name', 'short_info', 'published_at', 'updated_at', )
    # list_editable = ('price', 'discount', 'paid', 'free',  'category', )

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = (
        ('Portfolio Content', {
            "fields": (
                ('name', 'slug', 'short_info', 'description', )
            ),
        }),
        ('Main Image', {
            "fields": (
                'image',
                'caption',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }
    
admin.site.register(PortFolio, PortfolioAdmin)