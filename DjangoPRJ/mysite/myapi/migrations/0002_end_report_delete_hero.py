# Generated by Django 4.0.3 on 2022-04-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='End_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialnumber', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60)),
                ('symptomlabel', models.CharField(max_length=60)),
                ('location_id', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
