# Generated by Django 3.2 on 2021-07-20 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HFCCore', '0029_remove_project_funded_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_involvement', models.CharField(choices=[('Funding', 'Funding'), ('Execution', 'Execution'), ('Adoption', 'Adoption'), ('Promotion', 'Promotion')], max_length=50)),
                ('partner', models.ManyToManyField(blank=True, to='HFCCore.Partner')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HFCCore.project', verbose_name='Project')),
            ],
        ),
    ]
