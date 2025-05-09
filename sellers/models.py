from django.db import models
from django.contrib.auth.models import AbstractUser


class Seller(AbstractUser):
    username = models.CharField(
        unique=True, verbose_name="Имя", help_text="Укажите имя", max_length=50
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите тлф",
    )
    tg_nick = models.Charfield(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="TG ник",
        help_text="Укажите ник",
    )
    avatar = models.ImageField(
        upload_to="sellers/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Seller(Продавец)'
        verbose_name_plural = 'Sellers(Продавцы)'
