class Joueur:
    """Représente un joueur dans un tournoi."""

    def __init__(self, nom: str) -> None:
        if not nom or not nom.strip():
            raise ValueError("Le nom du joueur ne peut pas être vide.")
        self.nom = nom.strip()
        self.score = 0

    def gagner(self) -> None:
        """Incrémente le score du joueur de 1."""
        self.score += 1

    def __eq__(self, other) -> bool:
        if not isinstance(other, Joueur):
            return NotImplemented
        return self.nom == other.nom

    def __hash__(self) -> int:
        return hash(self.nom)
