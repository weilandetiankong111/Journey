# Generated by Django 2.0.4 on 2019-07-22 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_auto_20190722_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('fe72246f-9d06-4c33-acf8-ab2e6aa077c7'), verbose_name='用户jwt加密秘钥'),
        ),
    ]