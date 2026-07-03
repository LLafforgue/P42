## Une énumération :
Est un ensemble de noms symboliques (appelés membres) liés à des valeurs uniques,
Ils servent a etablir des constantes au sein du code. C'est une convention d'ecriture.
En C, Enum existe aussi mais il a deja des constantes implementees (Nord = 0, South = 1, ...).

Can be iterated over to return its canonical (i.e. non-alias) members in definition order

Utilise la syntaxe d'appel pour renvoyer les valeurs de ses membres,

Utilise la syntaxe d'indiçage pour renvoyer les noms de ses membres.


__Enum__ est la classe mère de toutes les énumérations.

```python
from enum import Enum

# class syntax

class Color(Enum):

    RED = 1

    GREEN = 2

    BLUE = 3

# functional syntax

Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
```
## Prefixer une valeur en py :

On peut prefixer en python une valeur pour indiquer si il s'agit d'une valeur en bit, ascii ...

```python
valeur_bit = 0b10
```
## Appels pour rester Package friendly:
```bash
py -m ex0.main
```
 - Python sait que ex0 est un package
 - les imports relatifs sont valides
