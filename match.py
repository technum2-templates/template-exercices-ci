import random

from joueur import Joueur


class Match:
    """Représente un match entre deux joueurs."""

    def __init__(self, joueur1: Joueur, joueur2: Joueur) -> None:
        # TODO : vérifier que joueur1 et joueur2 sont différents
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant: Joueur | None = None

    def jouer(self) -> Joueur:
        """Simule le match et désigne un gagnant aléatoirement."""
        # TODO : vérifier que le match n'a pas déjà été joué
        # TODO : choisir un gagnant aléatoirement parmi joueur1 et joueur2
        # TODO : incrémenter le score du gagnant
        # TODO : retourner le gagnant
        raise NotImplementedError


