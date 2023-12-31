# Generated by Django 3.0.3 on 2023-01-11 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20230111_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem',
            name='ACCESSCODE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mem',
            name='USERID',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buy',
            name='bdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 13, 47, 1, 782254, tzinfo=utc), verbose_name='兌換日期'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='IDCARD',
            field=models.CharField(max_length=10, null=True, verbose_name='身分證'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='NAME',
            field=models.CharField(max_length=10, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='NICKNAME',
            field=models.CharField(max_length=20, null=True, verbose_name='暱稱'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='PASSWORD',
            field=models.CharField(max_length=20, null=True, verbose_name='密碼'),
        ),
        migrations.AlterField(
            model_name='mem',
            name='PHONE',
            field=models.CharField(max_length=10, null=True, verbose_name='手機'),
        ),
    ]
