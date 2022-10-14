# Generated by Django 4.1.1 on 2022-10-03 18:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("test_api_generic", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthorGenericv2",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AuthorGenericv3",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
