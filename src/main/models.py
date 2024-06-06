"""
Модуль содержит классы моделей реализованных в приложении форм.
"""
from django.db import models
# Create your models here.

class Original(models.Model):
    '''
    Модель формы Original
    '''
    original_article = models.TextField()

class Translate(models.Model):
    '''
    Модель формы Translate
    '''
    translated_article = models.TextField()


class Summary(models.Model):
    '''
    Модель формы Summary
    '''
    summarize_article = models.TextField()
