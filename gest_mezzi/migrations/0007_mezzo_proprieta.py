# Generated by Django 2.0.2 on 2018-02-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_mezzi', '0006_auto_20180220_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='mezzo',
            name='proprieta',
            field=models.CharField(choices=[('NL', 'NOLEGGIO'), ('PC', 'PROPRIETA CONSORZIO'), ('PL', 'PROPIETA FERLOG LOG FER')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
