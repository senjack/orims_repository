# Generated by Django 2.0.2 on 2018-10-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orims', '0012_auto_20181023_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceunit',
            name='unit_type',
            field=models.CharField(choices=[('select', '--Select Category--'), ('Association', 'Association'), ('Business Firm', 'Business Firm'), ('Clinic', 'Clinic'), ('Club', 'Club'), ('Cooperative Society', 'Cooperative Society'), ('Drug Shop', 'Drug Shop'), ('Financial Institution', 'Financial Institution'), ('Group', 'Group'), ('Health Center', 'Health Center'), ('Hospital', 'Hospital'), ('Institute', 'Institute'), ('Institution', 'Institution'), ('Law Firm', 'Law Firm'), ('Media House', 'Media House'), ('Ministry', 'Ministry'), ('Organisation', 'Organisation'), ('Pharmacy', 'Pharmacy'), ('School', 'School'), ('Society', 'Society'), ('University', 'University'), ('Other', 'Others')], default='select', max_length=30, verbose_name='Service Unit Category'),
        ),
    ]