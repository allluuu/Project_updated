# Generated by Django 2.1.2 on 2018-10-24 08:56

from django.conf import settings
import django.contrib.auth.base_user
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0014_auto_20181024_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.ForeignKey(default=django.contrib.auth.base_user.AbstractBaseUser.get_username, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]