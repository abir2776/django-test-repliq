# Generated by Django 4.1.7 on 2023-03-12 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coassets', '0002_device_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='log',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='device',
            name='employee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='coassets.employee'),
        ),
    ]
