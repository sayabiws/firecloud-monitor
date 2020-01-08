# Generated by Django 3.0.1 on 2020-01-07 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200106_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='fire',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fires', to='api.Sensor'),
            preserve_default=False,
        ),
    ]
