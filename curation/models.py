from django.db import models

from product.models import Product


class Season(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name


class Curation(models.Model):
    title = models.CharField(max_length=100)
    seasons = models.ManyToManyField(Season, related_name="curations")
    colors = models.ManyToManyField(Color, related_name="curations")
    products = models.ManyToManyField(Product, related_name="curations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()
