# Generated by Django 4.2.4 on 2023-08-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]