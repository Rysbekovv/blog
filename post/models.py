from django.db import models
from django.conf import settings 
# Create your models here.

class Tag(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField()

    def __str__(self):
        return self.title()

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'


class Post(models.Model):

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор', related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    slug = models.SlugField(verbose_name='Слаг')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Фото', null=True, blank=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        