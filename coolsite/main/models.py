from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    task = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(verbose_name='Изображение', upload_to='photos/%Y/%m/%d/')
    date_create = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='Изменено', auto_now=True)
    cat = models.ForeignKey('Categories', verbose_name='Категории', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основые задачи'
        verbose_name_plural = 'Основные задачи'
        ordering = ['-date_create']


class Categories(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
