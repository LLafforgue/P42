# Fonctions et mécanismes Python pour l'accès dynamique et l'introspection

| Nom | Fonctionnalités | Arguments | Retour |
|----|-----------------|-----------|--------|
| `getattr` | Accède dynamiquement à un attribut ; permet une valeur par défaut si absent | `obj, name[, default]` | Valeur de l’attribut ou `default` |
| `hasattr` | Vérifie si un objet possède un attribut | `obj, name` | `bool` |
| `setattr` | Définit ou modifie dynamiquement un attribut | `obj, name, value` | `None` |
| `delattr` | Supprime dynamiquement un attribut | `obj, name` | `None` |
| `vars` | Retourne le dictionnaire d’attributs d’un objet | `obj` (optionnel) | `dict[str, Any]` |
| `dir` | Liste les attributs accessibles d’un objet | `obj` (optionnel) | `list[str]` |
| `callable` | Vérifie si un objet est appelable (fonction, méthode, etc.) | `obj` | `bool` |
| `isinstance` | Vérifie l’appartenance à un type ou protocole | `obj, type | tuple[type]` | `bool` |
| `issubclass` | Vérifie une relation d’héritage entre classes | `cls, type | tuple[type]` | `bool` |
| `type` | Retourne le type d’un objet ou crée une classe dynamiquement | `obj` ou `name, bases, dict` | `type` |
| `globals` | Accède au dictionnaire global courant | Aucun | `dict[str, Any]` |
| `locals` | Accède au dictionnaire local courant | Aucun | `dict[str, Any]` |
| `inspect.getmembers` | Liste les membres d’un objet (avec filtres possibles) | `obj[, predicate]` | `list[tuple[str, Any]]` |
| `inspect.isfunction` | Teste si un objet est une fonction | `obj` | `bool` |
| `inspect.ismethod` | Teste si un objet est une méthode liée | `obj` | `bool` |
| `__getattr__` | Intercepte l’accès à un attribut absent | `self, name` | Valeur |
| `__getattribute__` | Intercepte **tout** accès à un attribut | `self, name` | Valeur |
| `__dict__` | Stockage interne des attributs d’instance ou de module | Aucun | `dict[str, Any]` |
| `__all__` | Déclare les symboles exportés par `import *` | Liste de `str` | Convention (pas de retour) |
| `__mro__` | Ordre de résolution des méthodes (héritage complet) | `Classe` | `tuple[type, ...]` |

---

## Notes importantes (mypy)

- `getattr(obj, "x", None)` est **la solution la plus sûre** pour mypy
- `hasattr` **ne garantit pas** que l’attribut soit typé ou appelable
- `__all__` est **informatif**, pas contractuel pour le typage
- `__getattribute__` et `__getattr__` sont puissants mais **dangereux** pour la lisibilité et le typage
- Pour une API réellement typée → `Protocol` ou fichiers `.pyi`

---

## Recommandations rapides

| Besoin | Outil conseillé |
|------|----------------|
| Accès dynamique sûr | `getattr(..., default)` |
| Vérification simple | `hasattr` |
| API contractuelle | `Protocol` |
| Inspection/debug | `dir`, `vars`, `inspect` |
| Métaprogrammation avancée | `__getattr__`, `__getattribute__` |

---
## utilisation de -m
🔥 Les imports relatifs ne fonctionnent que dans des modules importés, jamais dans un script exécuté directement

```bash
python -m package.module
```
= “Exécute ce module comme faisant partie d’un package
”Python cherche le module dans sys.path (`__name__` est *package.module*)"
Sans le -m, `__name__` == `"__main__"`

| Élément        | Sans `-m`    | Avec `-m`                          |
| -------------- | ------------ | ---------------------------------- |
| Chargement     | fichier brut | module du package                  |
| `__name__`     | `"__main__"` | `"alchemy.transmutation.advanced"` |
| `__package__`  | `None`       | `"alchemy.transmutation"`          |
| Import relatif | ❌            | ✅                                  |
