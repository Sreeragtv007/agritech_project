# Generated by Django 4.2 on 2024-12-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_rename_crop_name_farmerdata_cropname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdata',
            name='time_stamb',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
