# Generated by Django 3.2.5 on 2021-11-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twophase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twophasevalue',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twophase.twophaseparticipant'),
        ),
    ]
