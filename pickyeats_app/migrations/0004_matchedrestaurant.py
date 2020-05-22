# Generated by Django 3.0.6 on 2020-05-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pickyeats_app', '0003_party_search_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchedRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('yelp_id', models.CharField(max_length=50)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickyeats_app.Party')),
            ],
        ),
    ]
