# Generated by Django 3.0.1 on 2020-01-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_fire_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fire',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
