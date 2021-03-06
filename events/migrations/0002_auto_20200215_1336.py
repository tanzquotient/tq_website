# Generated by Django 2.2 on 2020-02-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_squashed_0012_auto_20190904_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, help_text='Advertising image for this event.', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='special',
            field=models.BooleanField(blank=True, default=False, help_text='If this is a special event that should be emphasized on the website'),
        ),
    ]
