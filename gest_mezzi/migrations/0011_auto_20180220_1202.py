# Generated by Django 2.0.2 on 2018-02-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gest_mezzi', '0010_auto_20180220_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mezzo',
            name='proprieta',
            field=models.CharField(choices=[('NOLEGGIO', 'NOL'), ('PROPRIETA CONSORZIO', 'CONS'), ('PROPIETA FERLOG LOG FER', 'LOG FER')], max_length=30),
        ),
    ]