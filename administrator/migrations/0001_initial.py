# Generated by Django 2.0.2 on 2018-07-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_level', models.CharField(choices=[('unit-admin', 'Unit Level Administrator'), ('branch-admin', 'Branch Level administrator'), ('dept-admin', 'Department Level Administrator'), ('ofc-admin', 'Office Level Administrator'), ('select', 'Select Administrator Level')], default='select', max_length=30, verbose_name='Administrator Operation Scope')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Staff')),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
    ]
