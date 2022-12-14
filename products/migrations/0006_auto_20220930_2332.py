# Generated by Django 3.2.15 on 2022-09-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220928_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='country',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
