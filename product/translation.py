from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ('name', 'short_info', 'description')


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    field = ('name',)