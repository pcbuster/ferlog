# Generated by Django 2.0.2 on 2018-02-20 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gest_mezzi', '0016_auto_20180220_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mezzo',
            old_name='canonoe_noleggio_cliente',
            new_name='canone_noleggio_cliente',
        ),
        migrations.RenameField(
            model_name='mezzo',
            old_name='canonoe_noleggio_ferlog',
            new_name='canone_noleggio_ferlog',
        ),
        migrations.RenameField(
            model_name='mezzo',
            old_name='canonoe_noleggio_fornitore',
            new_name='canone_noleggio_fornitore',
        ),
    ]
