# Generated by Django 4.1.5 on 2023-01-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]