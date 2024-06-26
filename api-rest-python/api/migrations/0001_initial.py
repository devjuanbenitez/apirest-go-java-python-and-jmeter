# Generated by Django 5.0.4 on 2024-04-19 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "categoria",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "marca",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
                ("precio", models.FloatField()),
                ("stock", models.IntegerField()),
            ],
            options={
                "db_table": "producto",
                "managed": False,
            },
        ),
    ]
