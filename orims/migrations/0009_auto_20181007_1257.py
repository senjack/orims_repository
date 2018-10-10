# Generated by Django 2.0.2 on 2018-10-07 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orims', '0008_auto_20181005_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='registration_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='serviceunit',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_designation',
            field=models.CharField(choices=[('Official', 'Official'), ('receptionist', 'Receptionist'), ('select', '---Select Staff Designation---')], default='select', max_length=15, verbose_name='Designation'),
        ),
    ]
