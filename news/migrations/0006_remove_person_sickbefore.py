# Generated by Django 3.2.8 on 2021-10-24 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20211024_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='sickBefore',
        ),
    ]