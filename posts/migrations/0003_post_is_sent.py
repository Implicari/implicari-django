# Generated by Django 2.1.7 on 2019-02-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sent',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]