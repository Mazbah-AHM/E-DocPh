# Generated by Django 3.1.8 on 2021-06-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_prescription_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='complete',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
