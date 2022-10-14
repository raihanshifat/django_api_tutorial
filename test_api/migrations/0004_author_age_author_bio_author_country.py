# Generated by Django 4.1.1 on 2022-10-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_api", "0003_alter_author_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]