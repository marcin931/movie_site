# Generated by Django 3.1.4 on 2020-12-29 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0003_filmy_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmy',
            old_name='price',
            new_name='ticketPrice',
        ),
    ]
