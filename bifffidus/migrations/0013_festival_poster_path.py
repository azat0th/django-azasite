# Generated by Django 2.1.3 on 2019-02-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bifffidus', '0012_auto_20190223_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='poster_path',
            field=models.CharField(default='', max_length=200),
        ),
    ]