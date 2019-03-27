# Generated by Django 2.1 on 2019-03-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patienttriage',
            old_name='org',
            new_name='organization',
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patienttriage',
            name='arrival_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]