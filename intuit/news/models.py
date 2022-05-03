from django.db import models
from django.utils import timezone
from django.urls import reverse


class ActivePostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')

# Новость
class PostModel(models.Model):
    STATUS_CHOICES = (
        ("active", "активен"),
        ("passive", "не активен")
    )
    '''
        статус - status
        название - title
        ссылка - slug
        дата - date
        описание - description
        категории - categories
        изображения - images
        файлы - files
    '''
    
    objects = models.Manager()
    active_posts = ActivePostsManager()
    
    
    status = models.CharField(verbose_name="Статус", choices=STATUS_CHOICES, 
                                max_length=15, default="passive")


    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", unique_for_date='date')

    banner = models.FileField(verbose_name="Баннер", upload_to="news/images/banners",
                                blank=True)
    date = models.DateTimeField(verbose_name="Дата", default=timezone.now)
    description = models.TextField(verbose_name="Текст")
    
    categories = models.ManyToManyField('CategoryModel', related_name='categories',
                                        related_query_name="posts",verbose_name='Категории',)
    images = models.ManyToManyField('ImageModel', related_name='images',
                                        verbose_name='Фотографии', null=True, blank=True)
    files = models.ManyToManyField('FileModel', related_name='files',
                                        verbose_name='Файлы', null=True, blank=True)


    class Meta:
        ordering = ('-date',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


    def get_absolute_url(self):
        return reverse( 'news:new_detail', args=[self.date.year, 
                        self.date.month, self.date.day, self.slug])

    def __str__(self):
        return self.title
    
    
class CategoryModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка")

    class Meta:
        ordering = ('title',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    image = models.FileField(verbose_name="Изображение", upload_to="news/images/posts/%y/%m/%d",
                                null=True, blank=True)


    class Meta:
        ordering = ('title',)
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"


    def __str__(self):
        return self.title

class FileModel(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    file = models.FileField(verbose_name="Файл", upload_to="news/files/posts/%y/%m/%d", 
                                null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"    


    def __str__(self):
        return self.title