# Generated by Django 3.1.7 on 2021-06-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_achievement_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='field',
            field=models.CharField(choices=[('پرورشی', 'پرورشی'), ('آموزشی', 'آموزشی'), ('پژوهشی', 'پژوهشی'), ('ورزشی', 'ورزشی')], max_length=50),
        ),
    ]
