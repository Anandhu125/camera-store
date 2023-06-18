# Generated by Django 4.0.5 on 2023-05-25 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cam', '0008_alter_orders_expected_deliverydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 5, 30)),
        ),
        migrations.CreateModel(
            name='PartsCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('in-cart', 'in-cart'), ('order-placed', 'order-placed'), ('cancelled', 'cancelled')], default='in-cart', max_length=200)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('productparts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cam.camera')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CameraDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=300)),
                ('decriptio', models.CharField(max_length=200)),
                ('pric', models.PositiveBigIntegerField()),
                ('is_ctive', models.BooleanField(default=True)),
                ('imge', models.ImageField(blank=True, null=True, upload_to='images')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cam.camera')),
                ('categor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cam.category')),
            ],
        ),
    ]