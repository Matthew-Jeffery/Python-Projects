# Generated by Django 2.0.4 on 2018-06-16 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180616_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='highest_score',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='question_set',
        ),
        migrations.AddField(
            model_name='tournament',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='difficulty',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='start date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
