# Generated by Django 3.1.8 on 2021-05-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210426_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='authorize',
            field=models.BooleanField(default=False),
        ),
    ]
