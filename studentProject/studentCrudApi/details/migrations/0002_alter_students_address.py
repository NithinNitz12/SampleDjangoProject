# Generated by Django 3.2.4 on 2021-06-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
