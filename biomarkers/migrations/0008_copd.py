# Generated by Django 5.0 on 2023-12-25 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biomarkers', '0007_alter_cvd_cholesterol_level_hiv'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='COPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(null=True, verbose_name='Result')),
                ('AGE', models.IntegerField(blank=True, null=True, verbose_name='age')),
                ('PackHistory', models.BooleanField(blank=True, null=True, verbose_name='PackHistory')),
                ('MWT1', models.IntegerField(blank=True, null=True, verbose_name='1 minute walk test')),
                ('MWT2', models.IntegerField(blank=True, null=True, verbose_name='2 minute walk test')),
                ('FEV1', models.FloatField(blank=True, null=True, verbose_name='forced expiratory volume in 1 second')),
                ('FVC', models.FloatField(blank=True, null=True, verbose_name='forced vital capacity')),
                ('CAT', models.IntegerField(blank=True, null=True, verbose_name='COPD Assessment Test')),
                ('HAD', models.IntegerField(blank=True, null=True)),
                ('SGRQ', models.FloatField(blank=True, null=True, verbose_name="St George's Respiratory Questionnaire")),
                ('copd', models.BooleanField(blank=True, null=True, verbose_name='COPD')),
                ('gender', models.IntegerField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')])),
                ('smoking', models.BooleanField(blank=True, null=True, verbose_name='Smoker')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='copd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
