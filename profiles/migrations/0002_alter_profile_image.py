# Generated by Django 4.1.1 on 2022-09-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_images/default_profile.jpg', upload_to='profile_images/'),
        ),
    ]
