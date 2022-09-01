# Generated by Django 4.1 on 2022-08-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("author_name", models.CharField(max_length=255)),
                ("author_email", models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
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
                ("publisher_name", models.CharField(max_length=255)),
                ("publisher_email", models.EmailField(max_length=255)),
                ("publisher_site", models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Books",
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
                ("book_name", models.CharField(max_length=255)),
                ("book_price", models.IntegerField()),
                ("book_isbn", models.CharField(max_length=255)),
                ("book_published_date", models.DateField()),
            ],
            options={
                "unique_together": {("book_name", "book_isbn")},
            },
        ),
    ]
