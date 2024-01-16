# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,username,first_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('level','free')
        if other_fields.get('is_staff') is not True:
                raise ValueError(_('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
                raise ValueError(_('Please assign is_superuser=True for superuser'))
        return self.create_user(email,username,first_name,password,**other_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    username= models.CharField(_('User Name'),max_length=150)
    first_name = models.CharField(_('First Name'),max_length=150)
    last_name = models.CharField(_('last Name'),max_length=150)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    level = models.CharField(_('Level'), max_length=50, default='free')
    image = models.ImageField(upload_to='images/', blank=True)
    current_step=models.IntegerField(default=0)
    completed_all_steps=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=CustomAccountManager()
    phone = models.CharField(
        max_length=50,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=_("Enter a valid phone number.")
            )
        ]
    )
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name']
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        ordering = ['-id']  # Exemplo de ordenação padrão

    # Método para obter o nome completo do usuário
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Método para obter o nome curto do usuário
    def get_short_name(self):
        return self.first_name

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def __str__(self):
       return self.email

