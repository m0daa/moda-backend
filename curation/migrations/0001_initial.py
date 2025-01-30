# Generated by Django 5.1.5 on 2025-01-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "season",
                    models.CharField(
                        choices=[
                            ("spring", "봄"),
                            ("summer", "여름"),
                            ("fall", "가을"),
                            ("winter", "겨울"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("red", "레드"),
                            ("orange", "오렌지"),
                            ("yellow", "옐로우"),
                            ("green", "그린"),
                            ("blue", "블루"),
                            ("khaki", "카키"),
                            ("navy", "네이비"),
                            ("purple", "퍼플"),
                            ("black", "블랙"),
                            ("white", "화이트"),
                        ],
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="curations", to="product.product"
                    ),
                ),
            ],
        ),
    ]
