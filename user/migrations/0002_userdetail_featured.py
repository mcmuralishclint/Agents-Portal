# Generated by Django 2.2.4 on 2019-08-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]