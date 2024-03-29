# Generated by Django 2.0.5 on 2019-03-11 05:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disposition_type', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('time_of_death', models.DateTimeField(blank=True)),
                ('updated_condition', models.CharField(blank=True, max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury_type', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_last_name', models.CharField(blank=True, max_length=150)),
                ('patient_first_name', models.CharField(blank=True, max_length=150)),
                ('patient_middle_name', models.CharField(blank=True, max_length=150)),
                ('age', models.IntegerField(blank=True)),
                ('dob', models.DateTimeField(blank=True)),
                ('gender', models.CharField(blank=True, max_length=5)),
                ('unique_characteristics', models.CharField(blank=True, max_length=1000)),
                ('next_of_kin_name', models.CharField(blank=True, max_length=250)),
                ('next_of_kin_relation', models.CharField(blank=True, max_length=150)),
                ('next_of_kin_phone', models.CharField(blank=True, max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientTriage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('triage_tag_num', models.CharField(blank=True, max_length=50)),
                ('tag_color_condition', models.CharField(blank=True, max_length=25)),
                ('mode_of_arrival', models.CharField(blank=True, max_length=25)),
                ('arrival_date', models.DateTimeField(blank=True)),
                ('arrival_condition', models.CharField(blank=True, max_length=50)),
                ('room_number', models.CharField(blank=True, max_length=25)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Organization')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='injury',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
        ),
        migrations.AddField(
            model_name='disposition',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
        ),
        migrations.AddField(
            model_name='disposition',
            name='transfer_to_org',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='events.Organization'),
        ),
    ]
