from django.db import models
from django.utils import timezone


############ ANAGRAFICA ########

class Anagrafica(models.Model):
	data_creazione = models.DateField(default=timezone.now)
	nome = models.CharField(max_length=100, null=True, blank=True)
	cognome = models.CharField(max_length=100, null=True, blank=True)
	indirizzo = models.CharField(max_length=100, null=True, blank=True)
	citta = models.CharField(max_length=50)
	telefono = models.CharField(max_length=30, null=True, blank=True)
	note = models.TextField(max_length=500, null=True, blank=True)
	emailAziendale = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Email Az.')
	telefonoAziendale = models.CharField(max_length=50, null=True, blank=True)
	cellulareAziendale = models.CharField(max_length=50, null=True, blank=True)
	faxAziendale = models.CharField(max_length=50, null=True, blank=True)
	ragioneSociale = models.CharField(max_length=150, null=True, blank=True)
	piva = models.CharField(max_length=11, null=True, blank=True)
	cf = models.CharField(max_length=20, null=True, blank=True)

	def nuovo(self):
		self.data_creazione = timezone.now()
		self.save()

	def __str__(self):
		return self.nome, self.cognome, self.ragioneSociale

	def nome_intero(self):
		return u'%s %s' % (self.nome, self.cognome)

	class Meta:
		verbose_name_plural = "Aangrafiche"

############ CLIENTE ########

class Cliente(Anagrafica, models.Model):
	idCliente = models.AutoField(primary_key=True)
	indirizzoLegale = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.ragioneSociale

	class Meta:
		verbose_name_plural = "Clienti"

############ FORNITORI ########

class Fornitore(Anagrafica, models.Model):
	idFornitore = models.AutoField(primary_key=True)
	indirizzoLegale = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return '%s' % self.ragioneSociale

	class Meta:
		verbose_name_plural = "Fornitori"

############ IMPIANTI ########


class Impianto(models.Model):
    idImpianto = models.AutoField(primary_key=True)
    denominazione = models.CharField(max_length=100, null=True, blank=True)
    indirizzo = models.CharField(max_length=100, null=True, blank=True)
    citta = models.CharField(max_length=50)
    telefono_rif = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return '%s' % self.denominazione


    class Meta:
        verbose_name_plural = "Impianti"



############## IMMAGINI



############## STATO PROGETTO


TIPO_MEZZO = (
    ('GC', 'Golf-Car'),
    ('CE', 'Carrello-Elevatore'),
    ('CS', 'Carrello-Stoccatore'),
    ('T', 'Trattore'),
)
DURATA_NOLEGGIO = (
    ('1', '1 MESE'),
    ('2', '2 MESI'),
    ('3', '3 MESI'),
    ('4', '4 MESI'),
    ('5', '5 MESI'),
)

PROPRIETA_MEZZO = (
    ('NOLEGGIO','NOL'),
    ('PROPRIETA CONSORZIO','CONS'),
    ('PROPIETA FERLOG LOG FER','LOG FER'),
)



############ MEZZO ########

class Mezzo(models.Model):
    idMezzo = models.AutoField(primary_key=True)
    fornitore = models.ForeignKey(Fornitore, blank=True, on_delete=None)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=None)
    tipo = models.CharField(max_length=15, choices=TIPO_MEZZO)
    proprieta = models.CharField(max_length=30, choices=PROPRIETA_MEZZO)
    modello = models.CharField(max_length=100, null=True, blank=True)
    matricola = models.CharField(max_length=100, null=True, blank=True)
    matricola_fornitore = models.CharField(max_length=100, null=True, blank=True)
    descrizione = models.CharField(max_length=100, null=True, blank=True)
    colore = models.CharField(max_length=100, null=True, blank=True)
    ubicazione = models.ForeignKey(Impianto,on_delete=None)
    prezzo_acq = models.CharField(max_length=30, null=True, blank=True)
    canone_noleggio_fornitore = models.CharField(max_length=30, null=True, blank=True)
    canone_noleggio_ferlog = models.CharField(max_length=30, null=True, blank=True)
    canone_noleggio_cliente = models.CharField(max_length=30, null=True, blank=True)
    inizio_noleggio = models.DateField(blank=True, null=True)
    fine_noleggio = models.DateField(blank=True, null=True)
    durata_noleggio = models.CharField(max_length=15, choices=DURATA_NOLEGGIO)
    note = models.TextField(max_length=500, null=True, blank=True)
    immagine = models.ImageField(upload_to='mezzi', null=True, blank=True)
    #contratto =

    def __str__(self):
        return self.modello

    class Meta:
        verbose_name_plural = "Mezzi"



############ INTERVENTI ########

class Intervento(models.Model):
    idintervento = models.AutoField(primary_key=True)
    mezzo = models.ForeignKey(Mezzo, blank=True, on_delete=None)
    data_apertura = models.DateTimeField(auto_now_add=True)
    richiesto_da = models.CharField(max_length=100, null=True)
    dettagli = models.TextField(max_length=500, null=True, blank=True)
    fermo_dal = models.DateTimeField(blank=True, null=True)
    data_fine_riparazione = models.DateTimeField(blank=True, null=True)
    numero_giorni = models.CharField(max_length=5, null=True)
    preventivo_intervento = models.CharField(max_length=10, null=True,blank=True)
    costo_riparazione = models.CharField(max_length=10, null=True,blank=True)
    costo_cliente = models.CharField(max_length=10, null=True,blank=True)
    fattura_a = models.ForeignKey(Cliente,on_delete=None,blank=True,null=True)

    def __int__(self):
        return self.idintervento

    class Meta:
        verbose_name_plural = "Interventi"



