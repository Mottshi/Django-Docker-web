# Generated by Django 4.2.1 on 2023-05-25 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nickname', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(default='guest')),
            ],
            options={
                'db_table': 'Users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserLastCurrency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('currencyfrom', models.CharField(max_length=255)),
                ('currencyto', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Currency',
                'db_table': 'Currency',
                'managed': True,
            },
        ),
    ]
