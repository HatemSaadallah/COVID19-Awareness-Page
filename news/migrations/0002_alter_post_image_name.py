# Generated by Django 3.2.5 on 2021-08-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
