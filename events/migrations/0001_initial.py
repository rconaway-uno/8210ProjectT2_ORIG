# Generated by Django 2.0.5 on 2019-03-11 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(blank=True, max_length=25)),
                ('event_description', models.CharField(blank=True, max_length=250)),
                ('event_start_date', models.DateTimeField(blank=True)),
                ('event_end_date', models.DateTimeField(blank=True)),
                ('simulation_flag', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('end_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_type', models.CharField(blank=True, max_length=25)),
                ('org_name', models.CharField(blank=True, max_length=250)),
                ('org_addr1', models.CharField(blank=True, max_length=250)),
                ('org_addr2', models.CharField(blank=True, max_length=250)),
                ('org_city', models.CharField(blank=True, max_length=150)),
                ('org_state', models.CharField(blank=True, max_length=5)),
                ('org_zip', models.CharField(blank=True, max_length=10)),
                ('org_primary_phone', models.CharField(blank=True, max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='nurse',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Organization'),
        ),
    ]