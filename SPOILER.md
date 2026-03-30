# Spoiler -- Guide de résolution pas-à-pas

> Ne lis ce fichier qu'en dernier recours.

---

## Phase 1 : mettre en place le pipeline CI

### Créer le dossier et le fichier

Dans ton terminal (depuis la racine du repo) :

```bash
mkdir -p .github/workflows
cp ci.yml.template .github/workflows/ci.yml
```

Ou depuis l'explorateur de fichiers de VS Code : crée les dossiers manuellement.

### Compléter le fichier ci.yml

La ligne `run` doit lancer les tests :

```yaml
run: uv run python -m unittest discover
```

### Commit et push

```bash
git add .github/workflows/ci.yml
git commit -m "Mise en place du pipeline CI"
git push
```

Ou depuis l'onglet contrôle de version de VS Code : crée un commit puis synchronise-le.

### Vérifier sur GitHub

Va sur ton repo --> onglet "Actions". Tu dois voir un workflow qui tourne (cercle jaune) puis qui passe (coche verte).

Si c'est rouge : clique sur le workflow pour voir le message d'erreur.

---

## Phase 2 : implémenter `Match`

### Premier test : création d'un match

```python
def test_creation_match(self):
    m = Match(self.alice, self.bob)
    self.assertEqual(m.joueur1, self.alice)
    self.assertEqual(m.joueur2, self.bob)
```

Le `__init__` de `Match` stocke déjà `joueur1` et `joueur2` : ce test devrait passer.

### Empêcher un joueur de jouer contre lui-même

Test :

```python
def test_match_contre_soi_meme_leve_erreur(self):
    with self.assertRaises(ValueError):
        Match(self.alice, self.alice)
```

Code : dans `__init__`, ajouter la comparaison

```python
if joueur1 == joueur2:
    raise ValueError("Un joueur ne peut pas jouer contre lui-même.")
```

### Gagnant initial est None

Test :

```python
def test_gagnant_initial_est_none(self):
    m = Match(self.alice, self.bob)
    self.assertIsNone(m.gagnant)
```

Ce test passe déjà grâce au `__init__`.

### jouer() retourne un joueur

Test :

```python
def test_jouer_retourne_un_joueur(self):
    m = Match(self.alice, self.bob)
    gagnant = m.jouer()
    self.assertIn(gagnant, [self.alice, self.bob])
```

Code dans `jouer()` :

```python
self.gagnant = random.choice([self.joueur1, self.joueur2])
return self.gagnant
```

### jouer() incrémente le score du gagnant

Test :

```python
def test_jouer_incremente_score_du_gagnant(self):
    m = Match(self.alice, self.bob)
    gagnant = m.jouer()
    self.assertEqual(gagnant.score, 1)
```

Code : ajouter avant le `return` :

```python
self.gagnant.gagner()
```

### Jouer deux fois lève une erreur

Test :

```python
def test_jouer_deux_fois_leve_erreur(self):
    m = Match(self.alice, self.bob)
    m.jouer()
    with self.assertRaises(RuntimeError):
        m.jouer()
```

Code : ajouter au début de `jouer()` :

```python
if self.gagnant is not None:
    raise RuntimeError("Ce match a déjà été joué.")
```
