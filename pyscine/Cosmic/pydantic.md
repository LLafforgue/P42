## Filed

__Field__ sert à ajouter des contraintes, métadonnées et validations à un champ dans un modèle.
- d’ajouter des contraintes : gt (= greater than), lt, ge, le, ...
- de documenter (description)
- de définir une valeur par défaut, alias, etc.

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