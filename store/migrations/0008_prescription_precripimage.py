# Generated by Django 3.1.8 on 2021-06-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210608_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='precripImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]