# Generated by Django 3.0.4 on 2020-11-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0006_auto_20201117_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]