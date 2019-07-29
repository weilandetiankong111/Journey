# Generated by Django 2.0.4 on 2019-07-16 07:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20190715_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('609202bc-c114-4835-9484-8fe164851167'), verbose_name='用户jwt加密秘钥'),
        ),
    ]