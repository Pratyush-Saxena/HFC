# Generated by Django 3.2 on 2021-07-23 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0032_auto_20210723_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem_statement',
            old_name='title',
            new_name='brief',
        ),
        migrations.RenameField(
            model_name='problem_statement',
            old_name='summary',
            new_name='overview',
        ),
    ]
