# Generated by Django 2.1 on 2018-08-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitanja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='godine',
            field=models.IntegerField(default=2),
        ),
    ]
