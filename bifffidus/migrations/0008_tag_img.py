# Generated by Django 2.1.3 on 2019-02-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bifffidus', '0007_auto_20190223_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='img',
            field=models.CharField(default='', max_length=200),
        ),
    ]
