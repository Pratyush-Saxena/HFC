# Generated by Django 2.2.4 on 2020-04-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('website', models.URLField()),
                ('partner_desc', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/organization/')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('subdomain', models.CharField(blank=True, max_length=100)),
                ('thankyou_template', models.CharField(blank=True, max_length=500)),
                ('upi_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]