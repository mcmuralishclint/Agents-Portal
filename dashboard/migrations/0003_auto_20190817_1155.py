# Generated by Django 2.2.4 on 2019-08-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190817_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='schol_type',
            field=models.CharField(choices=[('F', 'Full Scholarship'), ('P', 'Partial Scholarship')], default='P', max_length=20),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='university',
            field=models.CharField(max_length=1),
        ),
    ]