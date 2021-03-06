# Generated by Django 4.0.3 on 2022-03-06 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0002_alter_breed_description_alter_rabbit_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquisition_date', models.DateField()),
                ('folio', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('note_date', models.DateField()),
                ('weight', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('weight_date', models.DateField()),
                ('rabbit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_app.rabbit')),
            ],
        ),
    ]
