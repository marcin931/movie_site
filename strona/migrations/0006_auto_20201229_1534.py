# Generated by Django 3.1.4 on 2020-12-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0005_auto_20201229_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
