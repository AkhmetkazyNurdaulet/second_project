from django.db import models

from django import forms

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class Tour(models.Model):
    tour_name = models.CharField(max_length=5000)
    tour_inf = models.CharField(max_length=5000)
    tour_id = models.IntegerField()

    def __str__(self):
        return self.tour_name


class Tourists(models.Model):
    CITIES = (
        ("1", "Almaty"),
        ("2", "Nursultan"),
        ("3", "Shymkent"),
        ("4", "Aktau"),
        ("5", "Other"),
    )

    CLASS = (
        ("1", "Eco"),
        ("2", "Vip"),
        ("3", "Lux"),
    )

    name = models.CharField(max_length=5000)
    phone_num = models.CharField(max_length=5000)
    email = models.EmailField(max_length=254)
    tour_id = models.IntegerField()
    discount = models.BooleanField(default="False")
    city = models.CharField(default=0, max_length=300, choices=CITIES)
    select_class = models.CharField(default=0, max_length=300, choices=CLASS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристтер"
        ordering = ['name', 'email']


class Info(models.Model):
    tour_name = models.CharField(max_length=5000)
    tour_price = models.CharField(max_length=5000)
    tour_inf = models.CharField(max_length=5000)
    time = models.TimeField(max_length=4000)
    tour_id = models.IntegerField()

    def __str__(self):
        return self.tour_name


class Posts(models.Model):
    title = models.CharField(max_length=250, verbose_name="Title")
    is_published = models.BooleanField(default=True, verbose_name="Tour")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



class Categories(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    describe = models.TextField(default='DataFlair Django')

    def __str__(self):
        return self.title




