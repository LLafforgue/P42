*This project has been created as part of the 42 curriculum by llafforg, osasburg.*

# Push_swap

## Summary
- [Description](#description)
- [Instructions](#instructions)
  - [Commandes de base](#commandes-de-base)
  - [Instructions de liste](#instructions-de-liste)
  - [Commandes de tri](#commandes-de-tri)
- [Algorithms](#algorithms)
  - [Parsing → Gestion des données](#parsing--gestion-des-données)
  - [Algorithme simple](#algorithme-simple)
  - [Algorithme intermédiaire : Bucket Sort](#algorithme-intermédiaire-bucket-sort)
  - [Algorithme complexe : Radix Sort](#algorithme-complexe-radix-sort)
- [Ressources](#ressources)

---

## Description
**Push_swap** est un programme qui trie un ensemble de `n` nombres entiers différents en utilisant deux **piles** (A et B) et des **opérations** contraintes (`sa`, `sb`, `ss`, `ra`, `rb`, `rr`, `rra`, `rrb`, `rrr`, `pa`, `pb`).

L'objectif est d'obtenir l'ensemble des nombres triés dans l'ordre croissant dans la **pile A**, en utilisant le moins d'opérations possible.
Ce programme de tri s'adapte au degré de désordre initial de l'ensemble selon trois échelons : *simple* (n ≤ 20), *medium* (0.2 < disorder ≤ 0.5), *complex* (disorder > 0.5). La stratégie de tri est **adaptative** ou **prédéfinie** par l'utilisateur. Le programme évalue la qualité du tri par le nombre total d'**opérations** employées.

---

## Instructions

### Commandes de base
1. **Compiler le programme** :
   ```bash
   make
   ```
2. **Exécuter le programme** :
   ```bash
   ./push_swap <votre liste de nombres>
   ```
   Exemple :
   ```bash
   ./push_swap 3 1 2
   ```
   Sortie :
   ```
   ra
   pb
   pa
   ```

### Instructions de liste
L'ensemble des nombres donnés en argument, contigus ou non, seront pris en compte dans leur ordre d'apparition sur la ligne de commande.\
Un nombre doit être séparé par un espace. Seuls les nombres entiers sont acceptés.\
La liste de nombres ne peut pas contenir de doublons.

Pour obtenir un descriptif du degré de désordre de la liste donnée, la stratégie de tri et le descriptif des opérations, utilisez l'option `--bench` :
```bash
./push_swap --bench 0 2 5 1 10 3 -5 8
```
Exemple de sortie :
```
[bench] n:              8
[bench] disorder:       39.28%
[bench] strategy:       Adaptive / O(n²)
[bench] total ops:      23
[bench] sa: 0   sb: 0   ss: 0   pa: 6   pb: 6
[bench] ra: 7   rb: 0   rr: 0   rra: 4  rrb: 0  rrr: 0
```

### Commandes de tri
Pour adapter la **strategie** de trie, l'utilisateur peut choisir de preciser ce dernier : `--simple` pour utiliser l'algorithme par extraction d'un extremum, `--medium` pour utiliser le trie par *bucket* et `--complex` pour utliser le tri avec *radix*.\
Sans precision de la commande de tri, le programme execute la strategie *adaptative*:
```bash
./push_swap 3 1 2 5 0 --bench --medium
```
Exemple de sortie :
```
[bench] n:              5
[bench] disorder:       60.00%
[bench] strategy:       O(n√n)
[bench] total ops:      12
[bench] sa: 0   sb: 0   ss: 0   pa: 3   pb: 3
[bench] ra: 5   rb: 1   rr: 0   rra: 0  rrb: 0  rrr: 0
```

---

## Algorithms

### Parsing → Gestion des données
Les données sont récupérées depuis la ligne de commande, vérifiées (pas de doublons, entiers valides), puis stockées dans une structure de pile (`t_stack`).\
La pile A recueille les données.\
Le parsing inclut :
- Vérification des arguments.
- Conversion en entiers.
- Détection des doublons.
- Calcul du degré de désordre initial.
Les données sont accessibles sous forme normalisées par leur rang (ex : a->rank[0] = 0). Pour créer cette normalisation il est nécessaire de trier fictivement les données. Cela est fait via un *quick sort*.

### Algorithme simple
Pour les petites listes (`désodre inférieur a 0,2` exclu ou `n < 20`), un **tri par insertion optimisé** est utilisé :
- **Stratégie** : Trouver le minimum de la liste et appliquer les rotations minimales pour le pusher sur la stack tampon (B). Puis réinsertion sur la stack initiale (A).
- **Complexité** : O(n²) dans le pire cas, mais très efficace pour n ≤ 5.

### Algorithme intermédiaire : Bucket Sort
Pour les listes de taille moyenne (`désodre entre 0,2 et 0,5` exclu), un **tri par buckets** est utilisé :
- **Stratégie** :
  - Diviser la pile en √n buckets en utilisant des quantiles.
  - Transférer les éléments vers la pile B par buckets.
  - Trier chaque bucket dans B (tri par insertion pour les petits buckets).
  - Remonter les éléments triés dans A.
- **Complexité** : O(n × √n) en moyenne.


### Algorithme complexe : Radix Sort
Pour les grandes listes (de `désodre supérieur a 0,5`), un **Radix Sort en base 2** est utilisé :
- **Stratégie** :
  - Trier les nombres en base 3 (semble optimisé pour notre version de l'algorithme).
  - Utiliser alternativement les piles A et B a chaque ordre de grandeur du chiffre traité (unité sur B--> 'ordre 1' sur A --> 'ordre 2' sur B -->...)
  - L'agorithme utilise des données normalisées au rang de tri. Ainsi l'ordre de grandeur maximal est celui de `n`.
- **Complexité** : O(n log n)

---

## Ressources
- **Documentation** :
  - [Sujet officiel 42](https://github.com/42School/norminette/blob/master/pdf/push_swap.fr.pdf)
- **Algorithmes** :
  - [Bucket Sort (Wikipedia)](https://en.wikipedia.org/wiki/Bucket_sort)
  - [Radix Sort (Wikipedia)](https://en.wikipedia.org/wiki/Radix_sort)
- **Outils** :
  - [Norminette](https://github.com/42School/norminette) (pour vérifier la norme 42).
  - [Valgrind](https://valgrind.org/) (pour détecter les fuites mémoire).
- **Autres** :
  - [Communauté 42]()

---
**Auteurs** : [llafforg](https://github.com/llafforg), [osasburg](https://github.com/osasburg)
