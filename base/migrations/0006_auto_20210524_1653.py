# Generated by Django 3.1.7 on 2021-05-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210520_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='field',
            field=models.CharField(choices=[('پرورشی', 'پرورشی'), ('آموزشی', 'آموزشی'), ('پژوهشی', 'پژوهشی'), ('پژوهشی', 'ورزشی')], max_length=50),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='level',
            field=models.CharField(choices=[('مدرسه', 'مدرسه'), ('ناحیه', 'ناحیه'), ('شهر', 'شهر'), ('استان', 'استان'), ('کشور', 'کشور'), ('بین الملل', 'بین الملل')], max_length=50),
        ),
    ]
