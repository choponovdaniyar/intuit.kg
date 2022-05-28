from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


admin.site.register(QuestionModel)


@admin.register(ChoiceProgram)
class ChoiseProgramAdmin(admin.ModelAdmin):
    list_display = ("user", "phone","email", "date", "status")
    readonly_fields = ("date", "user", "phone", "type", "profile", "edu_form", "place", "employment", "email")
    date_hierarchy = "date"
    list_filter = ("status","type", "profile", "edu_form", "place", "employment")
    ordering = ('-date',)
    list_editable = ("status",)

@admin.register(InteresUserModel)
class InteresUerAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "email", "category","date", "status"]
    readonly_fields = ("user", "phone", "category", "date", "email")
    date_hierarchy = "date"
    list_filter = ("category", "status")
    ordering = ('-date',)
    list_editable = ("status",)

@admin.register(PartnersModel)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_logo']
    readonly_fields = ["get_logo"]
    search_fields = ["title"]

    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' height=100>")
    
    get_logo.short_description = "логотип"

