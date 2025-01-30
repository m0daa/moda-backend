from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("outer", "아우터"),
        ("top", "상의"),
        ("bottom", "하의"),
        ("shoes", "신발"),
        ("bag", "가방"),
        ("accessories", "악세사리"),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.IntegerField(default=0)
    image_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
