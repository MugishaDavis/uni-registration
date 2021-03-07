# Generated by Django 3.1.5 on 2021-02-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=7)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.application')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.department')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.department'),
        ),
    ]
