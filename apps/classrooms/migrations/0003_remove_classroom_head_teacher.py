# Generated by Django 3.2.5 on 2021-07-20 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='head_teacher',
        ),
    ]