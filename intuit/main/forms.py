from django import forms
from django.core.mail import send_mail

from . import models
from intuit import settings



class InteresUser(forms.ModelForm):
    class Meta:
        model = models.InteresUserModel
        fields = [
            "user",
            "phone",
            "email"
        ]
        widgets = {
            'user': forms.TextInput(attrs={
                "type": "text",
                "class": "form-input",
                "placeholder": "Ваше имя"
            }),
            'phone': forms.NumberInput(attrs={
                "type": "tel",
                "class": "form-input",
                "placeholder": "Ваш номер телефона"
            }),
            'email': forms.NumberInput(attrs={
                "type": "email",
                "class": "form-input",
                "placeholder": "Ваш e-mail"
            })
        }

    def save(self,page, *args, **kwargs):
        kwargs["commit"] = False
        user = super().save(*args, **kwargs)
        user.category = models.InteresCategoryModel.objects.get_or_create(
                    title=page)[0]
        kwargs["commit"] = True
        user = super().save(*args, **kwargs)
        return user


    def send_message(self, title):
        user = self.data["user"]
        phone = self.data["phone"]
        email = self.data["email"]

        send_mail(
            "intuit.kg | {}".format(title),
            "ФИО: {}\nТелефон: {}\ne-mail: {}".format(user, phone, email),
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )


class ChoiceProgram(forms.ModelForm):
    class Meta:
        model = models.ChoiceProgram
        fields = [
            "type",
            "profile",
            "edu_form",
            "place",
            "employment",
            "user",
            "phone",
            "email"
        ]
        widgets = {
            "type": forms.TextInput(attrs={
                "type": "text"
            }),
            "profile": forms.TextInput(attrs={
                "type": "text"
            }),
            "edu_form": forms.TextInput(attrs={
                "type": "text"
            }),
            "place": forms.TextInput(attrs={
                "type": "text"
            }),
            "employment": forms.TextInput(attrs={
                "type": "text"
            }),
            "user": forms.TextInput(attrs={
                "placeholder": "Ваше имя*"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Ваш номер телефона*",
                "type": "text"
            }),
            "email": forms.TextInput(attrs={
                "placeholder": "Ваш e-mail*",
                "type": "text"
            }),
        }

    def send_message(self, title):
        user = self.data["user"]
        phone = self.data["phone"]
        email = self.data["email"]
        type = self.data["type"]
        profile = self.data["profile"]
        edu_form = self.data["edu_form"]
        place = self.data["place"]
        employment = self.data["employment"]

        send_mail(
            "intuit.kg | {}".format(title),

            f"ФИО: {user}\n"
            f"Телефон: {phone}\n"
            f"e-mail: {email}\n"
            f"Уровень образование {type}\n"
            f"Специальность {profile}\n"
            f"Форма обучения {edu_form}\n"
            f"Трудоустройство {place}\n"
            f"Бюджет {employment}",

            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )