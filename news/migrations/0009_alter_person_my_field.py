# Generated by Django 3.2.8 on 2021-10-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_person_my_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='my_field',
            field=models.CharField(choices=[('a', 'فايزر'), ('b', 'سبوتنيك'), ('c', 'سبوتنيك لايت'), ('d', 'موديرنا')], max_length=1),
        ),
    ]
