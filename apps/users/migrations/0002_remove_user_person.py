# Generated by Django 3.2.5 on 2021-07-18 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='person',
        ),
    ]
