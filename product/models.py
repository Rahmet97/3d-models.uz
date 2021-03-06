from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
# from urllib.parse import urlparse, parse_qs
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_('Kategoriya'))
    image = ImageField(upload_to="category/%Y/%m/%d/", blank=True, null=True, verbose_name=_('Kategoriya rasmi'))

    class Meta:
        ordering = ['name']
        verbose_name = _('Kategoriya')
        verbose_name_plural = _('Kategoriyalar')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Product(models.Model):
    model_file = models.FileField(upload_to="3D_File/%Y/%m/%d/", null=True, verbose_name=_("Model Fayl"))

    image = ImageField(upload_to="product/%Y/%m/%d/", verbose_name=_('Rasm'))
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name=_('Titr'))

    name = models.CharField(max_length=300, verbose_name=_('Nomi'))
    slug = models.SlugField(max_length=320)

    short_info = models.CharField(max_length=500, default="3D model", verbose_name=_("Qisqa ma'lumot"))
    description = models.TextField(verbose_name=_('Tavsif'))

    # price    = models.DecimalField( verbose_name='Price', max_digits=10, decimal_places=2, default=100, validators=( MinValueValidator(1), MaxValueValidator(100000000),))
    # discount = models.DecimalField( verbose_name='Discount', max_digits=10, decimal_places=2, blank=True, null=True, validators=( MinValueValidator(1), MaxValueValidator(100000000),))

    price = models.BigIntegerField(verbose_name=_('Narxi'), default=100,
                                   validators=(MinValueValidator(1), MaxValueValidator(100000000),))
    discount = models.BigIntegerField(verbose_name=_('Chegirma'), blank=True, null=True,
                                      validators=(MinValueValidator(1), MaxValueValidator(100000000),))

    paid = models.BooleanField(default=True, verbose_name=_("Pullik"))
    free = models.BooleanField(default=False, verbose_name=_("Bepul"))

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category',
                                 verbose_name=_('Kategoriya'))
    downloaded = models.IntegerField(default=0, verbose_name=_("Yuklab olindi"))

    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cart_field = models.BooleanField(default=False)  # this field is only changed through cart page

    class Meta:
        ordering = ['name', 'published_at', 'updated_at']
        verbose_name = _('3D Model')
        verbose_name_plural = _('3D Modellar')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_updated(self):
        if self.published_at == self.updated_at:
            return self.published_at
        else:
            self.updated_at

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Images(models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images", verbose_name=_("3D Model"))

    image = ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name=_("Rasm"))
    caption = models.CharField(max_length=300, blank=True, null=True, verbose_name=_('Titr:'))

    class Meta:
        verbose_name_plural = _("Model rasmi")

    def __str__(self):
        return self.model.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
