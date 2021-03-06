# Generated by Django 3.0.4 on 2020-11-15 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/admin/')),
                ('phone_number', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.IntegerField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=50)),
                ('case_type', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('type_of_weapon', models.CharField(blank=True, max_length=255)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('created_by', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin', to='admin_user.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('suspect_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/suspects')),
                ('phone_number', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('officer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='images/officer/')),
                ('department', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=50)),
                ('rank_of_officer', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin_officers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_officer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Criminal_Record',
            fields=[
                ('criminal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/criminal_record')),
                ('phone_number', models.CharField(max_length=12)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('relation', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.Case')),
                ('suspect_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admin_user.Suspect')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='officer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='officers', to='admin_user.Officer'),
        ),
    ]
