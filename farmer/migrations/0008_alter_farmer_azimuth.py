# Generated by Django 4.2 on 2024-12-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0007_farmer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='azimuth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
