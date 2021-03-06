# Generated by Django 4.0.5 on 2022-06-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0002_rename_task_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population',
            name='admin_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='population',
            name='capital',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='population',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='population',
            name='iso2',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
