# Generated by Django 2.2.4 on 2019-08-17 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_scholarship_service_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('tuition', models.IntegerField(default=0)),
                ('accomodation', models.IntegerField(default=0)),
                ('logo', models.ImageField(upload_to='logo/')),
            ],
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.University'),
        ),
    ]
