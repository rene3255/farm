# Generated by Django 4.0.3 on 2022-03-06 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0003_supply_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rabbit',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rabbit_breed', to='farm_app.breed'),
        ),
    ]
