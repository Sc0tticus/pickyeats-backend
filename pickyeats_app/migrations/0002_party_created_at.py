# Generated by Django 3.0.6 on 2020-05-16 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pickyeats_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
