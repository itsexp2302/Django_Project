# Generated by Django 4.0.6 on 2022-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]