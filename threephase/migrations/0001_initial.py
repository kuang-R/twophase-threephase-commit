# Generated by Django 3.2.5 on 2021-12-02 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwoPhaseParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('state', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TwoPhaseValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
                ('prepared_value', models.CharField(max_length=64)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threephase.twophaseparticipant')),
            ],
        ),
    ]
