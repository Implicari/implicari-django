# Generated by Django 3.2.5 on 2021-07-09 04:15

from django.db import migrations, models
import evaluations.models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluation',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='evaluation',
            name='order',
            field=models.PositiveIntegerField(default=evaluations.models.get_default_order),
        ),
    ]