# Generated by Django 4.2 on 2023-04-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='TimbakTu', max_length=20, verbose_name='City'),
        ),
    ]
