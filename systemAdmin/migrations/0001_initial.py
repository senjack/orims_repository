# Generated by Django 2.0.2 on 2018-07-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('system_admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('system_admin_user_name', models.CharField(max_length=254)),
                ('system_admin_password', models.CharField(max_length=254)),
                ('system_admin_email', models.EmailField(max_length=150)),
            ],
        ),
    ]
