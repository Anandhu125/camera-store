# Generated by Django 4.0.5 on 2023-05-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0018_specialorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialorders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cam.specialproduct'),
        ),
    ]
