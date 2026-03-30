import random

from joueur import Joueur
from match import Match


class Tournoi:
    """Représente un tournoi à élimination directe."""

    def __init__(self, joueurs: list[Joueur]) -> None:
        # TODO : vérifier qu'il y a au moins 2 joueurs
        self.joueurs: list[Joueur] = list(joueurs)
        self.matchs: list[Match] = []
        self.tour_actuel: int = 0

    def tour_suivant(self) -> list[Match]:
        """Joue un tour : chaque paire de joueurs restants s'affronte."""
        # TODO : vérifier que le tournoi n'est pas terminé
        # TODO : mélanger les joueurs aléatoirement
        # TODO : créer et jouer les matchs paire par paire
        # TODO : si nombre impair, le dernier joueur passe directement
        # TODO : mettre à jour self.joueurs avec les gagnants
        # TODO : incrémenter self.tour_actuel
        raise NotImplementedError

    def est_termine(self) -> bool:
        """Retourne True si le tournoi est terminé (un seul joueur restant)."""
        # TODO
        raise NotImplementedError

    def champion(self) -> Joueur | None:
        """Retourne le champion si le tournoi est terminé, sinon None."""
        # TODO
        raise NotImplementedError
