# Generated by Django 5.0 on 2023-12-23 17:11

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biomarkers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stroke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(null=True, verbose_name='Result')),
                ('glucose_level', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(150)], verbose_name='Glucose level')),
                ('bmi', models.FloatField(blank=True, default=None, help_text=None, null=True, verbose_name='BMI')),
                ('blood_pressure_systolic', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(70), django.core.validators.MaxValueValidator(300)], verbose_name='Blood pressure systolic')),
                ('blood_pressure_diastolic', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(150)], verbose_name='Blood pressure diastolic')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(13), django.core.validators.MaxValueValidator(110)], verbose_name='Age')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stroke', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
