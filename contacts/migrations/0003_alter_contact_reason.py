# Generated by Django 4.1.1 on 2022-09-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_content_alter_contact_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(max_length=50),
        ),
    ]