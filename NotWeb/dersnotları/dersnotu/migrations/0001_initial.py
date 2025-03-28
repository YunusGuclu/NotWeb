# Generated by Django 5.0.8 on 2024-08-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kategori",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tarifler",
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
                ("ad", models.CharField(max_length=100)),
                ("aciklama", models.TextField()),
                ("resim", models.ImageField(upload_to="resimler")),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
