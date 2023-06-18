# Generated by Django 4.0.5 on 2023-05-28 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cam', '0015_specialproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialproduct',
            old_name='camera_name',
            new_name='product_name',
        ),
        migrations.AlterField(
            model_name='specialcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cam.specialproduct'),
        ),
    ]
