# Generated by Django 4.0.5 on 2023-05-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0006_alter_cameradetails_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='company_name',
            field=models.CharField(choices=[('Canon', 'Canon'), ('Sony', 'Sony'), ('Panasonic', 'Panasonic'), ('Nikon', 'Nikon'), ('Fujifilm', 'Fujifilm'), ('Olympus', 'Olympus')], default='Canon', max_length=300),
        ),
        migrations.AlterField(
            model_name='cameradetails',
            name='company',
            field=models.CharField(max_length=300),
        ),
    ]