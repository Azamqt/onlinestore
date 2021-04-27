from django.db import models
from user.models import Profile


class Language(models.Model):
    language = models.CharField(max_length=30, verbose_name='Язык')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class ProgrammingLanguages(models.Model):
    language = models.CharField(max_length=30, verbose_name='Язык программирований')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Язык программирований'
        verbose_name_plural = 'Языки программирований'


class Courses(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тема')
    text = models.TextField(verbose_name='Описание')
    video = models.FileField(null=True, blank=True, verbose_name='Видео')
    image = models.ImageField(null=True, blank=True, max_length=100, verbose_name='Изображение')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='teacher', verbose_name='Учитель')

    rating = models.IntegerField(null=True, blank=True, verbose_name='Рейтинг')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='languages', verbose_name='Язык')

    programming_languages = models.ManyToManyField(ProgrammingLanguages, related_name='programming_languages',
                                                   verbose_name='Язык программирований')

    tags = models.CharField(max_length=50,null=True, blank=True, verbose_name='Теги')
    release_date = models.DateField(auto_now=True, verbose_name='Дата выхода')
    duration_course = models.IntegerField(null=True, blank=True, verbose_name='Длительность курса')
    time = models.TimeField(null=True, blank=True, verbose_name='Время')
    count_of_lections = models.IntegerField(null=True, blank=True, verbose_name='Количество лекций')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

