# Generated by Django 3.1.8 on 2021-06-24 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210619_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='contact_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
