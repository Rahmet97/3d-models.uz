from django_filters import CharFilter
import django_filters
from .models import Product
from django.db import models


class ProductFilter(django_filters.FilterSet):
    name=CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        fields=['name', 'slug', 'short_info', 'description', 'price', 'discount']
        # exclude=['']