# Generated by Django 5.1.1 on 2024-11-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=50),
        ),
    ]
