# Generated by Django 4.2 on 2024-12-11 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploadedimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farmerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('elevation', models.CharField(blank=True, max_length=50, null=True)),
                ('accuracy', models.CharField(blank=True, max_length=50, null=True)),
                ('azimuth', models.CharField(blank=True, max_length=50, null=True)),
                ('pitch', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('farmer_id', models.IntegerField(blank=True, null=True)),
                ('farmer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('crop_name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farmer.uploadedimage')),
            ],
        ),
    ]
