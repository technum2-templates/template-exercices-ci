import unittest

from joueur import Joueur
from match import Match


class TestMatch(unittest.TestCase):
    def setUp(self):
        self.alice = Joueur("Alice")
        self.bob = Joueur("Bob")

    # TODO : écrire les tests un par un, en suivant le cycle TDD :
    #   1. Écrire un test (rouge)
    #   2. Commit + push --> le pipeline échoue
    #   3. Écrire le code de production (vert)
    #   4. Commit + push --> le pipeline passe


if __name__ == "__main__":
    unittest.main()
