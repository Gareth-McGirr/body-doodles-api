# Generated by Django 4.1.1 on 2022-09-22 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='profile',
        ),
    ]