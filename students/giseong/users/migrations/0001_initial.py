# Generated by Django 3.2.9 on 2022-04-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=128, unique=True)),
                ('user_password', models.CharField(max_length=128)),
                ('user_phone_number', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]