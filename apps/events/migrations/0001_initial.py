# Generated by Django 3.2.5 on 2021-07-02 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateField(verbose_name='fecha')),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='update timestamp')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='classrooms.classroom')),
            ],
        ),
    ]
