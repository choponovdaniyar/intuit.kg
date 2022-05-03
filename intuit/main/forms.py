from django import forms

from . import models

import re


class InteresUser(forms.ModelForm):
    class Meta:
        model = models.InteresUserModel
        fields = [
            "user",
            "phone"
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
            })
        }

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