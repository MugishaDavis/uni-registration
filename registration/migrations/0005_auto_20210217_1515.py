# Generated by Django 3.1.5 on 2021-02-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(max_length=70),
        ),
    ]
