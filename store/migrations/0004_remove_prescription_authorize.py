# Generated by Django 3.1.8 on 2021-06-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_prescription_authorize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='authorize',
        ),
    ]