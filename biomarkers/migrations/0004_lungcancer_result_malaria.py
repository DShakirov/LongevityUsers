# Generated by Django 5.0 on 2023-12-24 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biomarkers', '0003_lungcancer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lungcancer',
            name='result',
            field=models.BooleanField(null=True, verbose_name='Result'),
        ),
        migrations.CreateModel(
            name='Malaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(null=True, verbose_name='Result')),
                ('image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Malaria', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
