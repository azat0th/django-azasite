# Generated by Django 2.1.3 on 2019-02-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bifffidus', '0010_auto_20190223_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='img_path',
        ),
    ]
