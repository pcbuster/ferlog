from django.contrib import admin

from gest_mezzi.models import Cliente, Fornitore, Mezzo, Impianto, Intervento

##############FORNITORI
class FornitoreAdmin(admin.ModelAdmin):
    list_display = ("idFornitore","ragioneSociale",'piva','nome','cognome')
    search_fields = ("idFornitore","ragioneSociale",'piva','nome','cognome')
    fieldsets = [
        ('Anagrafica Aziendale',{
            'fields': ['ragioneSociale','piva' , 'cf' , ]
        }),
        ('Referente', {
            'fields' : ['nome', 'cognome','telefono','emailAziendale']
        }),
    ]

admin.site.register(Fornitore,FornitoreAdmin)

##############CLIENTI
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("idCliente","ragioneSociale",'piva','nome','cognome')
    search_fields = ("IdCliente","ragioneSociale",'piva','nome','cognome')
    fieldsets = [
        ('Anagrafica Aziendale',{
            'fields': ['ragioneSociale','piva' , 'cf' , ]
        }),
        ('Referente', {
            'fields' : ['nome', 'cognome','telefono','emailAziendale']
        }),
    ]

admin.site.register(Cliente,ClienteAdmin)

##############MEZZI

class MezzoAdmin(admin.ModelAdmin):
    list_display = ("matricola","modello","cliente","canone_noleggio_cliente","inizio_noleggio","fine_noleggio","ubicazione","durata_noleggio","proprieta",)
    list_filter = ("ubicazione","cliente","proprieta",)
    search_fields = ("matricola",)

admin.site.register(Mezzo,MezzoAdmin)

##############IMPIANTO

class ImpiantoAdmin(admin.ModelAdmin):
    list_display = ("denominazione","indirizzo","citta","telefono_rif")

admin.site.register(Impianto,ImpiantoAdmin)



##################INTERVENTI

class InterventoAdmin(admin.ModelAdmin):
    list_display = ("idintervento","mezzo","data_apertura","fermo_dal","data_fine_riparazione","costo_cliente")
    list_filter = ("data_fine_riparazione","data_apertura")

admin.site.register(Intervento,InterventoAdmin)