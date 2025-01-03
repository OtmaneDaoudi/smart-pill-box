# Generated by Django 4.2.11 on 2024-12-03 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0002_alter_intake_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intake',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='intake',
            name='patient',
        ),
        migrations.AddField(
            model_name='intake',
            name='prescription',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='medication.prescription'),
        ),
    ]
