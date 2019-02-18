# Generated by Django 2.1.3 on 2019-02-18 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bifffidus', '0002_auto_20190214_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default='unknown', max_length=200)),
                ('jobname', models.CharField(default='unknown', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='crew',
            name='department',
        ),
        migrations.AlterField(
            model_name='crew',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_person', to='bifffidus.Job'),
        ),
    ]
