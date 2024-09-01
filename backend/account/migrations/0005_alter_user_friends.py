# Generated by Django 5.1 on 2024-09-01 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_user_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="friends",
            field=models.ManyToManyField(
                blank=True, to=settings.AUTH_USER_MODEL, verbose_name="друзья"
            ),
        ),
    ]