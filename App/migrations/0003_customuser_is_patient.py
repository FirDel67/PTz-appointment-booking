# Generated by Django 5.1.1 on 2024-11-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_customuser_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
    ]
