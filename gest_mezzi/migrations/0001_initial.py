# Generated by Django 2.0.2 on 2018-02-20 09:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anagrafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_creazione', models.DateField(default=django.utils.timezone.now)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cognome', models.CharField(blank=True, max_length=100, null=True)),
                ('indirizzo', models.CharField(blank=True, max_length=100, null=True)),
                ('citta', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('note', models.TextField(blank=True, max_length=500, null=True)),
                ('emailAziendale', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email Az.')),
                ('telefonoAziendale', models.CharField(blank=True, max_length=50, null=True)),
                ('cellulareAziendale', models.CharField(blank=True, max_length=50, null=True)),
                ('faxAziendale', models.CharField(blank=True, max_length=50, null=True)),
                ('ragioneSociale', models.CharField(blank=True, max_length=150, null=True)),
                ('piva', models.CharField(blank=True, max_length=11, null=True)),
                ('cf', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Aangrafiche',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('anagrafica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='gest_mezzi.Anagrafica')),
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('indirizzoLegale', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Clienti',
            },
            bases=('gest_mezzi.anagrafica', models.Model),
        ),
        migrations.CreateModel(
            name='Fornitore',
            fields=[
                ('anagrafica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='gest_mezzi.Anagrafica')),
                ('idFornitore', models.AutoField(primary_key=True, serialize=False)),
                ('indirizzoLegale', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Fornitori',
            },
            bases=('gest_mezzi.anagrafica', models.Model),
        ),
    ]
