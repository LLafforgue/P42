# Apprendre à construire des abstractions puissantes

Comprendre le rôle du modèle d’environnement (portée lexicale) dans l’exécution des fonctions.
Introduire des outils pratiques comme :
* les lambda expressions
* les decorators
* les fonctions retournant des fonctions (closures)

## Sommaire:
- [Fonction d'ordre superieur](#fonction-dordre-superieur)
- [Une closure](#une-closure)
- [Fonctions retournees (Closures)](#fonctions-retournees-closures)
- [Portée lexicale](#portee-lexicale)
- [Non Local](#non-local)
- [notion de Cell](#notion-de-cell)
- [Decorateurs](#decorateurs)
- [Expressions lambda](#expressions-lambda)
- [Les callables](#les-callables)
- [functools](#functools)
- [operator](#operator)

## Fonction d'ordre superieur

Une fonction d’ordre supérieur est une fonction qui :
* prend une fonction en argument
* et/ou retourne une fonction
Cela permet de capturer des schémas généraux de calcul et de les réutiliser.

Les fonctions d’ordre supérieur sont des fonctions qui manipulent d’autres fonctions (en arguments ou en résultats), ce qui permet de créer des abstractions puissantes.

* Elles permettent de factoriser du code
* Elles rendent les programmes plus modulaires
* Elles sont au cœur de la programmation fonctionnelle

```python

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

```

## Une closure

Quand une fonction est définie :

-> Elle capture :

les variables locales visibles à cet endroit
et les garde avec elle.

On appelle ça __une closure__ (= fonction + environnement)

Une fonction n’est pas juste du code.
Elle est composée de *fonction = (code, environnement)*

## Fonctions retournees (Closures)

Une fonction peut retourner une autre fonction qui “se souvient” de son environnement.

* C’est lié à la [Portée lexicale](#portee-lexicale).

## Portée lexicale

Dans un langage à portée lexicale, une fonction conserve l’environnement dans lequel elle a été définie, même après avoir été retournée.
La portée lexicale signifie : Une fonction utilise les variables définies là où elle est écrite, pas là où elle est appelée.

Lors de la __définition__ :
capture de l’environnement

Lors de __l’exécution__ :
recherche des variables dans cet environnement

* Une fonction “se souvient” des variables visibles lors de sa création
* Cela permet les closures

```python

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
add5(3)  # → 8

#adder se souvient de n = 5
```

## Non Local

Si vous essayez de modifier une variable immuable du scope parent, Python va considérer que vous souhaitez créer une nouvelle variable locale. Cela provoquerait une erreur.
Il faut indiquer spécifiquement que l'on souhaite modifier la variable locale capturée par la closure via le mot-clé `nonlocal` :

```python

import random as r
from typing import Callable

# Erreur
def creer_mot() -> Callable:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    a = ''

    def mot() -> str:
        a += r.choice(alpha)
        return a

    return mot

# Bon - ajout de nonlocal
def creer_mot() -> Callable:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    a = ''

    def mot() -> str:
        nonlocal a
        a += r.choice(alpha)
        return a

    return mot

mot= creer_mot()
mot2= creer_mot()
print(mot()) # Affiche 'o'
print(mot()) # Affiche 'ok'
print(mot2()) # Affiche 'j'
print(mot2()) # Affiche 'ja'
```

## notion de cell
La cell est un __conteneur persistant__ créé par Python pour qu'__une variable locale survive à la fin de sa fonction d'origine__, accessible uniquement par les closures qui la capturent.

Imagine sans cell, une closure naive :

```python
def mage_counter():
    n = 0
    def count():
        n += 1  # quel "n" ? celui de mage_counter qui n'existe plus !
    return count

count = mage_counter()
count()  # mage_counter est terminée... n a disparu ?

```

Quand `mage_counter()` se termine, normalement toutes ses variables locales sont **détruites**. Mais `count` en a encore besoin ! C'est le problème que la cell résout.

---

### La cell : un conteneur intermédiaire persistant

Python détecte à la compilation que `n` est capturée par `count`. Il ne met donc **jamais** `n` dans la ___stack normale___. Il crée une cell :
```
SANS closure          AVEC closure

stack de               Heap (mémoire longue durée)
mage_counter:          ┌──────────────┐
┌───────┐              │ CELL         │
│  n=0  │              │  ┌────────┐  │
└───────┘              │  │ int: 0 │  │
 disparaît !           │  └────────┘  │
                       └──────┬───────┘
                              │ persiste tant que
                              │ count existe
                       ┌──────┴───────┐
                       │   count()    │
                       └──────────────┘
```

### Cycle de vie d'une cell

```python
def mage_counter():
    n = 0                    # 1. Python crée une CELL pour n
    def count():
        nonlocal n
        n += 1               # 2. count accède à n via la cell
        return n
    return count             # 3. mage_counter se termine...
                             #    mais la cell SURVIT car count la référence

count = mage_counter()       # 4. count garde la cell en vie
count()                      # → 1   (cell contient maintenant 1)
count()                      # → 2   (cell contient maintenant 2)
del count                    # 5. plus personne ne référence la cell
                             #    → Python la détruit (garbage collector)
```

---

## Decorateurs

Un decorator est une syntaxe spéciale permettant d’appliquer une fonction d’ordre supérieur à une fonction lors de sa définition.

Un decorator :

* prend une fonction
* retourne une nouvelle fonction modifiée

```python

def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    '''Triple a int'''
    return 3 * x

#Equivalent sans decorateur
#def triple(x):
#    return 3 * x

#triple = trace(triple)

```
L'inconvenient de cette methode est que l'on perd des informations sur la fonction decoree (ici triple).
Exemple:
```python
print(triple.__name__) # "wrapper"
print(triple.__doc__) # None
```
Pour eviter cela on utilise [`wraps`](#wraps) de la bibliotheque `functools`.

## Expressions lambda

Fonctions anonymes (sans nom).

```python
#Exemple 1
lambda x: x * x

#Exemple 2
def compose1(f, g):
    return lambda x: f(g(x))
```

## Les callables

C’est un __objet__ que l’on peut appeler. Appeler un objet consiste à utiliser l’opérateur `()`, en lui précisant un certain nombre d’arguments, de façon à recevoir une valeur de retour. Cela cache une methode speciale : La méthode est ici _call__, dont les paramètres seront les arguments passés lors de l’appel.
En Python, on peut vérifier qu’un objet est appelable à l’aide de la fonction `callable`.

==> Problemes possibles:
* Pas assez d'arguments
* Trop d'arguments
* Mélange d'arguments positionnels et nommés

On retrouve l’opérateur `splat (*)`, il nous permet ici de récupérer la liste (ou plus précisément le tuple) des __arguments positionnels__ passés lors d’un appel, on appelle cela le __packing__.

```python
def func(foo, bar, *args):
     print(foo)
     print(bar)
     print(args)

#appel de func
func(1, 2, 3, 'a', 'b', None)
#Output :
>>> 1
>>> 2
>>> (3, 'a', 'b', None)
```
==> Il est possible de relayer les paramètres reçus par une fonction à une autre fonction, sans les préciser explicitement.

```python

def addition_3(a, b, c):
     return a + b + c

def proxy_addition_3(*args, **kwargs):
        return addition_3(*args, **kwargs)

```

Autre (que `def` pour une fonction ou `class` pour une classe) facon de generer son callable:
```python
class MyCallable:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a + b
```

## functools
### partial :
La fonction `partial` : celle-ci permet de réaliser un appel partiel de fonction, c'est a dire de generer un nouveau __callable__ qui encapsule (wrappe) la fonction orgiginale avec des arguments pres fixes.

exemple :
```python
def plus(x: int, y: int) -> int: #fonction originale
    return x + y

x_sub_5 = partial(plus, y=-5) #On fixe x a 5 mais ne propose pas encore de y.
print(x_sub_5(3)) # >>8
plus_1 = partial(plus, 1)
print(plus_1(3)) # >>4
```
### reduce :
Elle fonctionne de maniere assez similaire au `Array.reduce((acc,n)=>a + n, ini)` en JS avec :
* `acc` l'__accumulateur__,
* `n` l'__itere__ (ou element courant) de l'iterable Array
* `ini`la __valeur initiale__ optionnelle.

Dans le cas de reduce en python, l'utilisation est la suivante :

* reduce(__callable__, __Iterable__, __initialiseur__=None) => retourne une valeur unique

### wraps:
Est une fonction qui permet de faire des decorateur sans perdre d'information sur la fonction wrappee.

Exemple :
```python

from functools import wraps

def mon_decorateur(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Avant")
        return func(*args, **kwargs)
    return wrapper

@mon_decorateur
def ma_fonction(name: str) -> str:
    """Ma docstring"""
    return "Bravo " + name.capitalize()

print(ma_fonction.__name__)  # "ma_fonction"
print(ma_fonction.__doc__)   # "Ma docstring"

```
wraps(func) copie automatiquement :

* _name__
* _doc__
* _module__
* _annotations__
* ajoute _wrapped__ qui permet de garder le lien avec la fonction originale (ici ma_fonction) et ainsi de l'appeler sans declencher le decorateur (donc sans print "Avant").

### Mise en cache - lru_cache

Supposons que nous devions résoudre un problème mathématique et que nous passions une heure à trouver la bonne réponse. Si nous devions résoudre le même problème le lendemain, il serait utile de réutiliser notre travail précédent plutôt que de tout recommencer.

La mise en cache en Python suit un principe similaire : elle stocke les valeurs lorsqu'elles sont calculées dans les appels de fonction afin de les réutiliser lorsque cela est nécessaire. Ce type de mise en cache est également appelé mémorisation.

Voici une mise en cache manuelle :

```python
import random
import timeit # pour mesure le temps d'execution d'une fonction

sum_digits.my_cache = {} # cache manuel

def sum_digits(numbers: list[int]): # Fonction qui somme les chiffre d'une liste de nombres
    if numbers not in sum_digits.my_cache:
        sum_digits.my_cache[numbers] = sum(
            int(digit) for number in numbers for digit in str(number)
        )
    return sum_digits.my_cache[numbers]

numbers = tuple(random.randint(1, 1000) for _ in range(1_000_000))

print(
    timeit.timeit(
        "sum_digits(numbers)",
        globals=globals(),
        number=1
    )
)

print(
    timeit.timeit(
        "sum_digits(numbers)",
        globals=globals(),
        number=1
    )
)
```

Voici une mise en cache facilite par le decorateur __@lru_cache__
```python
import functools
import random
import timeit # pour mesure le temps d'execution d'une fonction

@functools.lru_cache
def sum_digits(numbers):
    return sum(
        int(digit) for number in numbers for digit in str(number)
    )

numbers = tuple(random.randint(1, 1000) for _ in range(1_000_000))

print(
    timeit.timeit(
        lambda: sum_digits(numbers),
        globals=globals(),
        number=1
    )
)

print(
    timeit.timeit(
        lambda: sum_digits(numbers),
        globals=globals(),
        number=1
    )
)
```

Le sigle « lru » au début du nom de la fonction signifie « least recently used » (moins récemment utilisé). Par défaut, le cache stocke les 128 premières valeurs calculées. Une fois les 128 emplacements occupés, l'algorithme supprime la valeur la moins récemment utilisée
Nous pouvons définir une taille maximale différente pour le cache lorsque nous décorons la fonction à l'aide du paramètre `maxsize`.
Exemple : `@functools.lru_cache(maxsize=5)` On ne stocke que 5 valeurs au lieu de 128.

Il existe d'autres stragtegies de mise en cache.

### Polymorphisme - singledispatch
__singledispatch__ permet le polymorphisme basé sur le type du premier argument.
Python regarde le type du premier argument puis choisit la bonne version.
Uniquement le premier argument est regarde.
Il evite les `isinstance()`
Pour ajouter des surcharges d'implémentation à la fonction, utiliser l'attribut `register()` de la fonction générique. Le type souhaité peut être passé explicitement en argument au décorateur.

Exemple:
```python
from functools import singledispatch

@singledispatch
def affiche(x):
    print("Type inconnu")

@affiche.register
def _(x: int):
    print("Entier :", x)

@affiche.register(str)
def _(x):
    print("Texte :", x)

affiche(10)       # Entier : 10
affiche("hello")  # Texte : hello
affiche(3.14)     # Type inconnu

```

## operator
voir [docs python - operator](https://docs.python.org/3/library/operator.html)



## Ressources

* [zeste de savoir](https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/1-callables/)
* [docs python - functools](https://docs.python.org/3/library/functools.html)
* [caches](https://www.datacamp.com/fr/tutorial/python-cache-introduction)