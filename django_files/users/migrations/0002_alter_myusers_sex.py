# Generated by Django 4.1.4 on 2023-01-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'male'), ('Female', 'female'), ('Not Say', 'Not Say')], max_length=50, null=True),
        ),
    ]
