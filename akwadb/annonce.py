__all__ = ['Annonce']
from enum import Enum
class Annonce(Enum):
    Salle_de_bain = 1
    Piece = 2
    Superificie = 3
    Garage = 4
    Baignoire = 5
__all__ = ['TypeAnnonce']
class TypeAnnonce(Enum):
    Location = 1
    Vente = 2
