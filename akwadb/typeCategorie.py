__all__ = ['TypeCategorie']
from enum import Enum
class TypeCategorie(Enum):
    Maison = 1
    Terrain = 2
    Bureau = 3
    Villa = 4
    Appartement = 5
    Studio = 6
    Location_vide = 7
    Location_meublé = 8
    Immeuble = 9
