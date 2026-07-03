*This project has been created as part of the 42 curriculum by llafforg*

[![42](https://img.shields.io/badge/42-Project-blue)](https://www.42.fr/)

**Printf** est un ensemble de fonction C dont le but est de fournir une fonction qui reproduit la fonction printf de la bibliotheque C stdio.

---

## Table des matieres
- [Description](#description)
    - [Fonctions](#fonctions)
- [Instructions](#instructions)
- [Utilisation](#instructions)
- [Algroithme](#algorithme)
- [Ressources](#ressources)

---

## Description
Ce projet consiste a reproduire printf. L'ensemble des fonctions est archive via `ft_print.h` en un document `libftprintf.a`. Chacune des fonctions de cette bibliotheque retourne le nombre de caracteres ecrits sur la sortie standard.

### Fonctions

| Fonction              | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| `ft_printf`           | Principale fonction reproduisant le comportement de printf.      |
| `ft_put_address`      | Afiche sur le l'adresse d'un pointeur sur la sortie standard.    |
| `ft_put_nbr`          | Affiche un nombre `int` sur la sortie standard.                  |
| `ft_put_str`          | Affiche une chaine de caracteres sur la sortie standard.         |
| `ft_put_unsigned_nbr` | Affiche un nombre `unsigned int` sur la sortie standard.         |
| `ft_put_unsigned_hex` | Affiche un `unsigned int` en hexadecimal sur la sortie standard. |

---

## Instructions
1. Clonez le depot :
```bash
git clone <https://github.com/42learners/Common-Core---Printf-2a493ae5-47b6-4825-abb8-3cb436e0f907.git>
   ```
2. Compilez la bibliotheque :
```bash
make
```
3. Incluez le fichier d'en-tete `ft_printf.h` dans votre projet et liez la bibliotheque lors de la compilation :
```bash
gcc -Wall -Wextra -Werror main.c -L. -lft -o programme
```
4. Pour effacer les fichiers .o et l'executable libft.a :
 ```bash
   make fclean
   ```
---

## Utilisation
Incluez `ft_printf.h` dans votre code et utilisez les fonctions comme suit :
```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("%dere regle du %s Club !", 1, "Fight");
}
```

---

## Algorithme
ft_printf est la fonction principale qui centralise l'ensemble.
La fonction ft_print est variadique. Elle contient un nombre de parametre definit par l'utilisateur.
On utilise la bibliotheque `stdarg` pour gerer cette suite de parametres.
La fonction ft_printf se structure en trois parties :
- <font color="blue">Verification</font>
- <font color="blue">Ecriture</font>
- <font color="blue">Retour</font>

La **premiere partie** de la fonction verifie que l'input textuel (*format*) du printf pour verifier que les *%* sont bien implemetes *ft_error*. Des ce moment, la fonction retoune -1 si l'entree ne respecte pas le format de printf.\
La partie **ecriture** avance dans la variable *format* et incremente au fur et a mesure la valeur de la longueur de la chaine de caracteres ecrite en sortie standard (*len*). A chaque *%*, la liste des parametres est incremente pour traiter la nature de la variable entree en parametres.\
Pour finir, la fonction **renvoie** la valeur de *len*.


---

## Ressources
- La communauté 42;
- gitbook.io;
- stackoverflow.com;
- https://github.com/Tripouille;

