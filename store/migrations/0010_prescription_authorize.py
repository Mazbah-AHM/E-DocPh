# Generated by Django 3.1.8 on 2021-06-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210609_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='authorize',
            field=models.BooleanField(default=False),
        ),
    ]