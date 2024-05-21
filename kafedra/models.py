from django.db import models
from enum import Enum


class PageType(Enum):
    MAIN_PAGE = 1
    FACULTY_HISTORY_PAGE = 2
    RESEARCH_WORK_PAGE = 3
    INTERNATIONAL_COOPERATION_PAGE = 4
    EMPLOYMENT_PAGE = 5

class Information(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    article_url = models.URLField(max_length=200, blank=True, null=True)
    page_type = models.IntegerField(null=True, blank=True, choices=[(tag.value, tag.name) for tag in PageType])
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class Employees(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo_employees/')
    article_url = models.EmailField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'