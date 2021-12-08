# Generated by Django 3.2.5 on 2021-07-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('is_archived', models.BooleanField(default=False, verbose_name='is archived')),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='update timestamp')),
            ],
            options={
                'verbose_name_plural': 'classrooms',
            },
        ),
    ]