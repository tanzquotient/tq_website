# Generated by Django 2.2.12 on 2020-04-25 15:08

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20200413_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfinancefile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/app/postfinance'), upload_to=''),
        ),
    ]