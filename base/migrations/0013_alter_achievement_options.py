# Generated by Django 3.2.3 on 2021-05-31 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20210530_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'permissions': (('parvareshi_mentor', 'can view parvareshi'), ('amoozeshi_mentor', 'can view amoozeshi'), ('pazhooheshi_mentor', 'can view pazhooheshi'), ('varzeshi_mentor', 'can view varzeshi'))},
        ),
    ]