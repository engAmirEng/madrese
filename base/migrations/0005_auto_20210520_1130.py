# Generated by Django 3.1.7 on 2021-05-20 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210519_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.student'),
        ),
    ]
