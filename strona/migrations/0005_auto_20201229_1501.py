# Generated by Django 3.1.4 on 2020-12-29 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0004_auto_20201229_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmy',
            old_name='cover',
            new_name='image',
        ),
    ]
