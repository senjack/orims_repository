# Generated by Django 2.0.2 on 2018-06-28 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orims', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='appointment_id',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='appointment_id',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff_id',
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]