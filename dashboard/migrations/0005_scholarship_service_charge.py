# Generated by Django 2.2.4 on 2019-08-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190817_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='service_charge',
            field=models.IntegerField(default=500),
        ),
    ]