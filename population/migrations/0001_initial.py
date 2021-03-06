# Generated by Django 4.0.5 on 2022-06-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=20)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=20)),
                ('country', models.CharField(max_length=200)),
                ('iso2', models.CharField(max_length=5)),
                ('admin_name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('population', models.DecimalField(decimal_places=10, max_digits=20)),
                ('population_proper', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]
