from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import PostModel, FileModel, ImageModel, CategoryModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "date"]
    list_filter = ['date', 'status', 'categories']
    ordering = ['-status', '-date']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    filter_horizontal = ['categories', 'files', 'images']
    date_hierarchy = 'date'
    list_editable = ['status']
    save_on_top = True
    save_as = True

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", 'image', 'photo']
    list_filter = ['title']
    search_fields = ['title']

    def photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100>")

@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ["title", "file"]

# Register your models here.
