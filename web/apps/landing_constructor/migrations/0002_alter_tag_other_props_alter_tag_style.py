# Generated by Django 4.1.7 on 2023-04-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing_constructor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="other_props",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="style",
            field=models.JSONField(blank=True, null=True),
        ),
    ]