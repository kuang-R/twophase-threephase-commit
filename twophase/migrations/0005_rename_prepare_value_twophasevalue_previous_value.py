# Generated by Django 3.2.5 on 2021-11-29 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twophase', '0004_rename_statue_twophaseparticipant_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twophasevalue',
            old_name='prepare_value',
            new_name='previous_value',
        ),
    ]
