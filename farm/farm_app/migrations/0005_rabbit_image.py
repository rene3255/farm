# Generated by Django 4.0.3 on 2022-03-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0004_alter_rabbit_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='rabbit',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]