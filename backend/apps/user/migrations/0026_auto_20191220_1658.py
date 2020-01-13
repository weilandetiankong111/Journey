# Generated by Django 2.0.4 on 2019-12-20 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20191219_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('1efda6cd-48a8-4610-8590-1f68098d9c19'), verbose_name='用户jwt加密秘钥'),
        ),
    ]