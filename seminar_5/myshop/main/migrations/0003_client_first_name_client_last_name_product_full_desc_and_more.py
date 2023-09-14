# Generated by Django 4.2.4 on 2023-09-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="first_name",
            field=models.CharField(default="Unnamed", max_length=100),
        ),
        migrations.AddField(
            model_name="client",
            name="last_name",
            field=models.CharField(default="Unnamed", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="full_desc",
            field=models.TextField(default="Описание отсутствует"),
        ),
        migrations.AddField(
            model_name="product",
            name="short_desc",
            field=models.CharField(default="Описание недоступно", max_length=100),
        ),
    ]