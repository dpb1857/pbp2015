# Generated by Django 2.1.5 on 2019-02-10 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='control',
            old_name='seq',
            new_name='location_id',
        ),
    ]
