from django.db import models


class SupportManage(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Имя менеджера", help_text="Укажите имя менеджера"
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
    tg_nick = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="TG ник",
        help_text="Укажите ник",
    )
    date_born = models.DateField(
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="supports/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    class Meta:
        verbose_name = "Support(Менеджер)"
        verbose_name_plural = "Supports(Менеджеры)"
