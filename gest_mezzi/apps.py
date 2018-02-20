from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class GestMezziConfig(AppConfig):
    name = 'gest_mezzi'



class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
