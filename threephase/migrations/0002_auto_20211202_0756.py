# Generated by Django 3.2.5 on 2021-12-02 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threephase', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TwoPhaseParticipant',
            new_name='ThreePhaseParticipant',
        ),
        migrations.RenameModel(
            old_name='TwoPhaseValue',
            new_name='ThreePhaseValue',
        ),
    ]
