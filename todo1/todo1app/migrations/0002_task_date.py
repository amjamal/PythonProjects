# Generated by Django 4.1.3 on 2022-12-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-02-03'),
            preserve_default=False,
        ),
    ]
