# Generated by Django 2.2.4 on 2019-08-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userdetail_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='country',
            field=models.CharField(default='China', max_length=100),
        ),
    ]