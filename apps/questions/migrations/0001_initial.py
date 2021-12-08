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
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='mensaje')),
                ('is_sent', models.BooleanField(default=False)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='update timestamp')),
            ],
            options={
                'ordering': ('creation_timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255, verbose_name='asunto')),
                ('message', models.TextField(verbose_name='mensaje')),
                ('is_sent', models.BooleanField(default=False)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('update_timestamp', models.DateTimeField(auto_now=True, verbose_name='update timestamp')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='classrooms.classroom')),
            ],
            options={
                'ordering': ('creation_timestamp',),
            },
        ),
    ]