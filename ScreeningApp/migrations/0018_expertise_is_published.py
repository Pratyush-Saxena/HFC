# Generated by Django 2.2.4 on 2021-03-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScreeningApp', '0017_question_question_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='is_published',
            field=models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=10, null=True),
        ),
    ]
