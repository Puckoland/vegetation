# Generated by Django 4.2.3 on 2023-11-04 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vegetation_app', '0001_squashed_0003_rename_water_tolerance_plant_drought_tolerance'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plant',
            name='water_frequency_winter',
            field=models.IntegerField(),
        ),
    ]