# Generated by Django 3.2.3 on 2021-05-31 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_achievement_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'permissions': (('parvareshi_mentor', 'can do parvareshi'), ('amoozeshi_mentor', 'can do amoozeshi'), ('pazhooheshi_mentor', 'can do pazhooheshi'), ('varzeshi_mentor', 'can do varzeshi'))},
        ),
    ]
