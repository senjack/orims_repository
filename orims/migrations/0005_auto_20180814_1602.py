# Generated by Django 2.0.2 on 2018-08-14 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orims', '0004_auto_20180814_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='sunit_id',
            new_name='unit_id',
        ),
    ]
