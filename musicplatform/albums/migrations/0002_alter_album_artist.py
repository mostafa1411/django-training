# Generated by Django 4.1.2 on 2022-10-12 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='artists.artist'),
        ),
    ]
