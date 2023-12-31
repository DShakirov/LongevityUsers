# Generated by Django 5.0 on 2023-12-21 14:13

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractEmailPhoneUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('cognito_username', models.UUIDField(default=uuid.UUID('f19c7a93-94af-4f5b-98df-8aa4fc6eed5e'), editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='email or phone')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_used', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_locked', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permanent_token', models.CharField(max_length=255, unique=True)),
                ('jwt_secret', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Device name')),
                ('details', models.CharField(blank=True, max_length=255, verbose_name='Device details')),
                ('last_request_datetime', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['-ip_address'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('abstractemailphoneuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.abstractemailphoneuser')),
            ],
            options={
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            bases=('users.abstractemailphoneuser',),
        ),
        migrations.AddField(
            model_name='abstractemailphoneuser',
            name='user_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_device', to='users.device'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
    ]
