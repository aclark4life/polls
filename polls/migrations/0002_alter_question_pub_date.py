# Generated by Django 5.0.10.dev20241112012728 on 2024-11-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(null=True, verbose_name="date published"),
        ),
    ]
