# Generated by Django 3.1.5 on 2021-02-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='name',
        ),
    ]