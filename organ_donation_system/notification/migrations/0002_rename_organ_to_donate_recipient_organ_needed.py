# Generated by Django 5.1.1 on 2024-10-25 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipient',
            old_name='organ_to_donate',
            new_name='organ_needed',
        ),
    ]
