# Generated by Django 3.1.3 on 2020-11-27 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201127_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]