# Generated by Django 3.0.3 on 2020-02-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='clue',
            field=models.CharField(default='', max_length=50),
        ),
    ]