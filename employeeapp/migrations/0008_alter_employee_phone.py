# Generated by Django 4.0.6 on 2022-07-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0007_employee_binary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
