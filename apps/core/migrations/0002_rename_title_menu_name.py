# Generated by Django 4.2.1 on 2023-08-03 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='name',
        ),
    ]
