# Generated by Django 2.1.3 on 2019-02-04 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bifffidus', '0011_auto_20190204_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_Movie_Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festival', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='festival_tag', to='bifffidus.Festival')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_tag', to='bifffidus.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='screening',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_type',
        ),
        migrations.DeleteModel(
            name='Tag_Type',
        ),
        migrations.AddField(
            model_name='tag_movie_festival',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag', to='bifffidus.Tag'),
        ),
    ]
