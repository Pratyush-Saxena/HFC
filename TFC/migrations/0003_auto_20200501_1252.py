# Generated by Django 2.2.4 on 2020-05-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TFC', '0002_auto_20200429_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='organization/'),
        ),
    ]
