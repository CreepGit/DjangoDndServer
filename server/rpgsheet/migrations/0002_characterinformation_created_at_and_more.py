# Generated by Django 4.1.5 on 2023-02-01 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpgsheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterinformation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 1, 10, 47, 16, 199631, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characterinformation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
