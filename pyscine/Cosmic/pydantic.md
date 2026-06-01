## Filed

__Field__ sert à ajouter des contraintes, métadonnées et validations à un champ dans un modèle.
- d’ajouter des contraintes : gt (= greater than), lt, ge, le, ...
- de documenter (description)
- de définir une valeur par défaut, alias, etc.

Exemple de fonctions utilisees dans Field:

| Paramètre | Type | Description | Exemple |
|---|---|---|---|
| `default` | `Any` | Valeur par défaut du champ si aucune valeur n'est fournie à l'instanciation. | `Field(default="inconnu")` |
| `description` | `str` | Texte descriptif du champ, intégré dans le schéma JSON généré (utile pour la documentation OpenAPI). | `Field(description="Nom complet de l'utilisateur")` |
| `pattern` | `str` | Expression régulière (regex) que la valeur de type `str` doit respecter. Lève une `ValidationError` si la valeur ne correspond pas. | `Field(pattern=r"^\d{5}$")` — code postal 5 chiffres |
| `ge` | `int \| float` | *Greater or Equal* — valeur numérique minimale **incluse**. Équivalent à `>=`. | `Field(ge=0)` — valeur ≥ 0 |
| `le` | `int \| float` | *Less or Equal* — valeur numérique maximale **incluse**. Équivalent à `<=`. | `Field(le=100)` — valeur ≤ 100 |
| `default_factory` | `Callable` | Fonction appelée **à chaque instanciation** pour produire la valeur par défaut. Indispensable pour les types mutables (`list`, `dict`, etc.) afin d'éviter le partage d'état entre instances. | `Field(default_factory=list)` |

> **Combinaison ge / le** : il est courant de les utiliser ensemble pour définir un intervalle : `Field(ge=0, le=100)` impose `0 ≤ valeur ≤ 100`.

---

## typing — `Annotated` et `Literal`

### `Annotated[T, ...]`

Permet d'**attacher des métadonnées** à un type sans en changer la sémantique de base.
Pydantic exploite ces métadonnées pour appliquer des validations directement dans la signature de type, évitant de répéter `Field(...)` sur chaque champ.

```python
from typing import Annotated
from pydantic import BaseModel, Field

Age = Annotated[int, Field(ge=0, le=150, description="Âge en années")]

class Personne(BaseModel):
    age: Age
```

---

### `Literal[val1, val2, ...]`

Restreint la valeur acceptée à un **ensemble fini de constantes** (chaînes, entiers, booléens…).
Pydantic lève une `ValidationError` si la valeur fournie ne fait pas partie des littéraux déclarés.

```python
from typing import Literal
from pydantic import BaseModel

class Commande(BaseModel):
    statut: Literal["en_attente", "validée", "annulée"]
    priorite: Literal[1, 2, 3]
```

> `Literal` est particulièrement utile pour modéliser des **énumérations légères** sans recourir à `enum.Enum`.

## Validator

__model_validator__ permet de creer une fonction de validation qui s'applique a plusieurs attributs.
Exemple:
```python
    @model_validator(mode='after')
    def validate_ID(self) -> Self:
	#...
```

__ValidationError__ Permet de gerer les erreurs *raised* dans le validator.
C'est une exception générée par Pydantic lorsqu'une ou plusieurs validations échouent.
* Dans un validator, on lève généralement :
* ValueError
* TypeError
* AssertionError

Il est appele dans le except et generalement au moment du `raise` il n'est pas appele (on raise `ValueError` par exemple) directement. Mais si l'on souhaite personnaliser et maitriser correctement l'ensemble du message d'erreur, on peut l'utiliser avec le module `.from_exception_data()`.

Exemple:
```python
	raise ValidationError.from_exception_data(
		title="AlienContact",
		line_errors=[
			{
				'type': 'value_error',
				'loc': ('is_verified',),
				'ctx': {'error': 'The report must be verified'},
				'input': f'Verified: {self.is_verified}',
			}
		],
		)
	#...
	except (ValidationError) as e:
	print('Unvalid station')
	for msg in e.errors():
		m = msg['loc'][0]
		print(f"\033[31m{m}\033[0m")
		print(msg.get('msg', 'Pas de message'))
```