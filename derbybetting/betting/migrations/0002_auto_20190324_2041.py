# Generated by Django 2.1.7 on 2019-03-24 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bet',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='bet',
            name='horse',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='person',
        ),
        migrations.DeleteModel(
            name='Bet',
        ),
        migrations.DeleteModel(
            name='Horse',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
