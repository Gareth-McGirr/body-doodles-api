# Generated by Django 4.1.1 on 2022-09-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_profile_is_artist_profile_artistid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='artistId',
            field=models.IntegerField(null=True),
        ),
    ]
