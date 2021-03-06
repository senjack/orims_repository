# Generated by Django 2.0.2 on 2018-10-18 03:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orims', '0010_auto_20181007_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='office',
            name='office_working_time',
            field=models.CharField(choices=[('Standard Working Time and Days', 'Standard Working Time and Days'), ('Set Custom Working Time for office', 'Set Custom Working Time for office')], default='Standard Working Dime and Days', max_length=30),
        ),
    ]
