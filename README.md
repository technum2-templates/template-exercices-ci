# Tournoi 1v1 -- CI avec GitHub Actions

## Objectif

Mettre en place un pipeline d'intégration continue (CI) et implémenter la classe `Match` en TDD.

## Ce que tu as déjà

- `joueur.py` et `test_joueur.py` : la classe `Joueur`, telle qu'elle a été construite en démo
- `match.py` : le squelette de la classe `Match` à compléter
- `test_match.py` : le fichier de tests de `Match`, vide pour l'instant -- c'est toi qui l'écris
- `tournoi.py` : bonus pour les plus rapides

## Phase 1 : mettre en place le pipeline CI (~30 min)

### Étapes

1. Dans ton repo, crée le dossier `.github/workflows/`
2. Copie le fichier `ci.yml.template` dans ce dossier sous le nom `ci.yml`
3. Complète les lignes marquées `# TODO`
4. Commit et push
5. Va sur GitHub --> onglet "Actions" --> vérifie que le pipeline passe au vert

### Lancer les tests en local

```bash
uv run python -m unittest discover
```

## Phase 2 : implémenter `Match` en TDD (~80 min)

Le cycle à suivre pour chaque fonctionnalité :

1. Écrire un test dans `test_match.py` --> les tests sont rouges
2. Commit + push --> le pipeline échoue (c'est normal !)
3. Écrire le code dans `match.py` pour faire passer le test --> les tests sont verts
4. Commit + push --> le pipeline passe au vert

### Fonctionnalités à implémenter

- Créer un match entre deux joueurs
- Empêcher un joueur de jouer contre lui-même
- `gagnant` est `None` avant de jouer
- `jouer()` retourne l'un des deux joueurs
- `jouer()` enregistre le gagnant dans `self.gagnant`
- `jouer()` incrémente le score du gagnant
- Jouer deux fois le même match lève une erreur

## Bonus : implémenter `Tournoi`

Si tu as terminé `Match`, complète `tournoi.py`. Les fonctionnalités attendues sont décrites dans les commentaires `# TODO`.

---

Bloqué ? Consulte `SPOILER.md`.
