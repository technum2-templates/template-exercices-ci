import unittest

from joueur import Joueur


class TestJoueur(unittest.TestCase):
    def test_creation_joueur(self):
        j = Joueur("Alice")
        self.assertEqual(j.nom, "Alice")

    def test_score_initial_est_zero(self):
        j = Joueur("Alice")
        self.assertEqual(j.score, 0)

    def test_gagner_incremente_le_score(self):
        j = Joueur("Alice")
        j.gagner()
        self.assertEqual(j.score, 1)

    def test_gagner_deux_fois(self):
        j = Joueur("Alice")
        j.gagner()
        j.gagner()
        self.assertEqual(j.score, 2)

    def test_nom_vide_leve_erreur(self):
        with self.assertRaises(ValueError):
            Joueur("")

    def test_nom_espaces_leve_erreur(self):
        with self.assertRaises(ValueError):
            Joueur("   ")

    def test_nom_est_strip(self):
        j = Joueur("  Alice  ")
        self.assertEqual(j.nom, "Alice")

    def test_egalite_par_nom(self):
        j1 = Joueur("Alice")
        j2 = Joueur("Alice")
        self.assertEqual(j1, j2)

    def test_inegalite_noms_differents(self):
        j1 = Joueur("Alice")
        j2 = Joueur("Bob")
        self.assertNotEqual(j1, j2)


if __name__ == "__main__":
    unittest.main()
