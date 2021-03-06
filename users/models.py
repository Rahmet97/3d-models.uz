from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, phone_number, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, phone_number, first_name, password, **other_fields)

    def create_user(self, email, phone_number, first_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_("Siz elektron pochta manzilingizni ko'rsatishingiz kerak"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Elektron pochta'), unique=True)
    # user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(_("Foydalanuvchi nomi"), max_length=150)    
    phone_number = models.CharField(_("Telefon raqami"), max_length=13, unique=True) # validators should be a list
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'biz haqimizda'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name']

    def __str__(self):
        return self.email