from django.db import models
from datetime import datetime


class ChoiceProgram(models.Model):
    STATUS_CHOISE = (
        ("active", "активный"),
        ("passive", "не активный")
    )
    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOISE, max_length=15,
                                default="active")
    date = models.DateTimeField(verbose_name="Дата регистрации", default=datetime.now())
    user = models.CharField(verbose_name="Имя", max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=25)
    email = models.CharField(verbose_name="e-mail", max_length=50)
    type = models.CharField(verbose_name="Тип", max_length=20)
    profile = models.CharField(verbose_name="Направление", max_length=100)
    edu_form = models.CharField(verbose_name="Форма обучения", max_length=20)
    place = models.CharField(verbose_name="Форма оплаты", max_length=20)
    employment = models.CharField(verbose_name="Трудоустройство", max_length=20)

    class Meta:
        ordering = ("date",)
        verbose_name = "Участник"
        verbose_name_plural = "Программа 'Выбор профессии'"

    def __str__(self):
        return self.user


class InteresUserModel(models.Model):
    STATUS_CHOISE = (
        ("active", "активный"),
        ("passive", "не активный")
    )
    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOISE, max_length=15,
                                default="active")
    date = models.DateTimeField(verbose_name="Дата регистрации", default=datetime.now())

    user = models.CharField(verbose_name="Имя", max_length=250)
    phone = models.CharField(verbose_name="Телефон", max_length=50)
    category = models.ForeignKey(verbose_name="Категория", on_delete=models.CASCADE,
                                to="InteresCategoryModel")

    class Meta:
        ordering = ("-date",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.user

class InteresCategoryModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)

    class Meta:
        ordering = ("title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class PartnersModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)
    logo = models.FileField(verbose_name="Логотип", upload_to="main/partners/logo/")

    class Meta:
        ordering = ("title",)
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.title

