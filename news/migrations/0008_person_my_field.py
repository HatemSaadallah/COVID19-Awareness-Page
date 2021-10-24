# Generated by Django 3.2.8 on 2021-10-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='my_field',
            field=models.CharField(choices=[('a', 'Hola'), ('b', 'Hello'), ('c', 'Bonjour'), ('d', 'Boas')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]