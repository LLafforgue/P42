# Dependances et installations


## Liste des dependances installees dans un environnement.
```bash
pip list
```

## Pour poetry

Explication des sections
[tool.poetry]

Contient les métadonnées du projet :

name : nom du package

version : version du projet

description : description courte

authors : auteur(s)

packages : dossier contenant le code Python

[tool.poetry.dependencies]

Dépendances nécessaires au fonctionnement :

python = "^3.10"
signifie >=3.10,<4.0

les packages :

pandas >=2.1.0

requests >=2.31.0

matplotlib >=3.7.2

[tool.poetry.group.dev.dependencies]

Dépendances de développement uniquement (tests, lint, etc.).

[build-system]

Section obligatoire pour indiquer le backend de build

### Commandes Poetry:
Commandes utiles avec Poetry

Initialiser l'environnement : `poetry install`

Ajouter une dépendance : `poetry add numpy`

Lancer un script : `poetry run python script.py`

Activer le shell : `poetry shell`

### Sélectionner le bon interpréteur

Dans VS Code :

	Ctrl + Shift + P
	Python: Select Interpreter
	Choisir : Python 3.13.x (/usr/bin/python3)
