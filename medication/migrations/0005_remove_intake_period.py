# Generated by Django 4.2.11 on 2024-12-03 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0004_alter_intake_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intake',
            name='period',
        ),
    ]