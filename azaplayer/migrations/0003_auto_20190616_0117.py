# Generated by Django 2.1.3 on 2019-06-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azaplayer', '0002_remove_audio_post_uploaded_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_post',
            old_name='audio_file',
            new_name='audiofile',
        ),
        migrations.AlterField(
            model_name='audio_post',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
