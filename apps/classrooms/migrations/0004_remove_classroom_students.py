# Generated by Django 3.2.10 on 2021-12-08 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0003_remove_classroom_head_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='students',
        ),
    ]
