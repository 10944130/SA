# Generated by Django 3.0.3 on 2023-01-09 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='bdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='兌換日期'),
        ),
    ]
