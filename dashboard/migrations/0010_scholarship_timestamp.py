# Generated by Django 2.2.4 on 2019-08-17 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_delete_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
