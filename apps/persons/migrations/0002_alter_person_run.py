# Generated by Django 3.2.5 on 2021-07-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='run',
            field=models.IntegerField(blank=True, null=True, verbose_name='RUN'),
        ),
    ]