# Generated by Django 4.1.5 on 2023-01-17 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sources',
            new_name='Source',
        ),
    ]