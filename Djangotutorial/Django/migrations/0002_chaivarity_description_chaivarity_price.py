# Generated by Django 5.0.6 on 2024-06-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
