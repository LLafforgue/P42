# OS_utils

__os.path.dirname()__ : Retourne le répertoire parent d’un chemin (tout ce qui est avant le dernier fichier ou dossier).

__os.sep__ : Le séparateur de dossiers utilisé par le système d’exploitation.

__os.walk()__ : permet de parcourir récursivement une arborescence de dossiers.

__os.system()__ : permet d'envoyer depuis un shell sous-processus des commandes de terminales. (obsolete -> utiliser la bibliotheque `subprocess`)

Elle génère successivement les chemins des répertoires rencontrés ainsi que les fichiers et sous-dossiers qu’ils contiennent.

Concrètement, os.walk() retourne à chaque itération un tuple de trois éléments :
* dirpath : le chemin du dossier courant
* dirnames : la liste des sous-dossiers présents dans ce dossier
* filenames : la liste des fichiers présents dans ce dossier

__os.environ__ est un objet du module Python os qui représente les variables d’environnement du système sous forme d’un dictionnaire modifiable.
Les clés sont les noms des variables d’environnement.
Les valeurs sont leurs contenus sous forme de chaînes de caractères.
Modifier os.environ modifie les variables d’environnement du processus courant (et celles héritées par ses sous-processus).

Exemple (python):
```python
import os

# Lire une variable d'environnement
path = os.environ.get("PATH")

# Définir / modifier une variable
os.environ["APP_MODE"] = "production"

# Supprimer une variable
del os.environ["APP_MODE"]
```


## Pour acceder aux variable d'environnement :

```python
	home = os.environ["HOME"]
	print(home)
```

Ou :

```python
	os.getenv("HOME")
```

## Informations générales

__PATH__ est la variable système utilisée par le système d'exploitation pour localiser les __fichiers exécutables__ indispensables depuis la ligne de commande ou la fenêtre de terminal.
La variable système PATH peut être configurée à l'aide de l'`utilitaire système` dans le Panneau de configuration sous Windows ou dans `le fichier de démarrage` du shell sous Linux et Solaris.
Vous n'avez pas forcément besoin de modifier la variable PATH système sur les ordinateurs fonctionnant sous Windows ou Mac OS X.

## Questions divers

### matrix_env/bin/python
venv/bin/python est simplement l'interpréteur Python du virtual environment.
Quand tu crées un environnement :
	python -m venv matrix_env
Il crée une copie (ou lien) de Python dans : matrix_env/bin/python

Quand tu l’utilises :
	matrix_env/bin/python mon_script.py
Tu exécutes Python avec cet environnement isolé.

Ce Python va automatiquement chercher les packages dans : matrix_env/lib/python3.11/site-packages

### Problemes de shell
```python
os.system(f'cd {dir_venv} && deactivate')
```
Ne peut pas fonctionner car os.system() lance un nouveau shell ([sous-processus](#-sous-processus) du shell parent). Or la commande `source matrix_env/bin/activate` modifie l'environnement du shell existant (shell parent). En effet, `deactivate` ne depend pas du dossier mais de du shell de l'environnement specifique a l'activation du venv (plus precisement : une fonction définie dans le shell lors de l'activation du venv).

### --rcfile

```bash
bash --rcfile myfile.sh
```

Bash :
1. démarre un shell interactif
2. ignore ~/.bashrc
3. charge myfile.sh à la place

Le script d’activation d’un venv `matrix_env/bin/activate` est justement un script qui :
1. modifie __PATH__
2. définit __VIRTUAL_ENV__
3. change le prompt

revenir a un environnement shell configure par .bashrc : `bash-5.2$ exit`
### -Sous-processus
Un processus est un programme en cours d’exécution dans le système.

Exemples :

* un terminal
* un script Python
* un navigateur

Chaque processus possède :
* son PID (identifiant)
* sa mémoire
* ses variables d’environnement
* ses ressources

Quand un programme lance un autre programme, on obtient :

	Terminal (processus parent)
			│
			└── Python script
					│
					└── commande lancée avec os.system()

Le programme lancé devient un sous-processus (child process).
