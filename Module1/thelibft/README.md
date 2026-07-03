*This project has been created as part of the 42 curriculum by llafforg*
---
[![42](https://img.shields.io/badge/42-Project-blue)](https://www.42.fr/)

**Libft** est une bibliotheque C recodee a partir de fonctions standard. Elle inclut des fonctions de manipulation de chaines de caracteres, de listes chainees et de gestion de memoire.

---

## Table des matieres
- [Description](#description)
- [Fonctions](#fonctions)
    - [Fonctions de la libc](#fonctions-de-la-libc)
    - [Fonctions supplémentaires](#fonctions-supplementaires)
- [Instructions](#instructions)
- [Utilisation](#instructions)
- [Ressources](#ressources)

---

## Description
Ce projet consiste a recoder certaines fonctions de la bibliotheque standard C (`libc`), accompagnees du prefixe ft_, ainsi que des fonctions utilitaires supplementaires.

---

## Fonctions

### Fonctions de la libc
| Fonction     | Description                                                       |
|--------------|-------------------------------------------------------------------|
| `ft_isalpha` | Verifie si un caractere est alphabétique.                         |
| `ft_isdigit` | Verifie si un caractere est un chiffre.                           |
| `ft_isalnum` | Verifie si un caractere est alphanumérique.                       |
| `ft_isascii` | Verifie si un caractere est ASCII.                                |
| `ft_isprint` | Verifie si un caractere est imprimable.                           |
| `ft_strlen`  | Calcule la longueur d'une chaîne de caracteres.                   |
| `ft_memset`  | Remplit une zone memoire avec un octet donne.                     |
| `ft_bzero`   | Met à zero une zone memoire.                                      |
| `ft_memcpy`  | Copie une zone memoire vers une autre.                            |
| `ft_memmove` | Copie une zone memoire vers une autre (version securisee).        |
| `ft_strlcpy` | Copie une chaine de caracteres de manière securisee.              |
| `ft_strlcat` | Concatène deux chaines de caracteres de maniere securisee.        |
| `ft_toupper` | Convertit un caractere en majuscule.                              |
| `ft_tolower` | Convertit un caractere en minuscule.                              |
| `ft_strchr`  | Recherche la premiere occurrence d'un caractere dans une chaine.  |
| `ft_strrchr` | Recherche la derniere occurrence d'un caractere dans une chaine.  |
| `ft_strncmp` | Compare deux chaines de caracteres sur `n` octets.                |
| `ft_memchr`  | Recherche un octet dans une zone memoire.                         |
| `ft_memcmp`  | Compare deux zones memoire.                                       |
| `ft_strnstr` | Recherche une sous-chaine dans une chaine.                        |
| `ft_atoi`    | Convertit une chaine en entier.                                   |
| `ft_calloc`  | Alloue et initialise une zone memoire.                            |
| `ft_strdup`  | Duplique une chaine de caracteres.                                |

### Fonctions supplementaires
| Fonction          | Description                                                                          |
|-------------------|--------------------------------------------------------------------------------------|
| `ft_substr`       | Extrait une sous-chaine d'une chaine.                                                |
| `ft_strjoin`      | Concatene deux chaines de caracteres.                                                |
| `ft_strtrim`      | Supprime les caracteres specifies au debut et à la fin d'une chaine.                 |
| `ft_split`        | Decoupe une chaine en un tableau de sous-chaines.                                    |
| `ft_itoa`         | Convertit un entier en chaine de caracteres.                                         |
| `ft_strmapi`      | Applique une fonction a chaque caractere d'une chaine.                               |
| `ft_striteri`     | Applique une fonction a chaque caractere d'une chaine avec son index.                |
| `ft_putchar_fd`   | Ecrit un caractere sur un descripteur de fichier.                                    |
| `ft_putstr_fd`    | Ecrit une chaine sur un descripteur de fichier.                                      |
| `ft_putendl_fd`   | Ecrit une chaine suivie d'un saut de ligne sur un descripteur de fichier.            |
| `ft_putnbr_fd`    | Ecrit un entier sur un descripteur de fichier.                                       |
| `ft_lstadd_back`  | Ajoute l'élément `new` à la fin de la liste.                                         |
| `ft_lstadd_front` | Ajoute l'élément `new` au début de la liste.                                         |
| `ft_lstclear`     | A l'aide de 'del' et free, supprime et libère la mémoire des l'élément d'une liste.  |
| `ft_lstdelone`    | A l'aide de 'del' et free, supprime la mémoire de l'élément passé en paramètre.      |
| `ft_lstiter`      | Parcoure une liste et appliquer la fonction `f` au contenu de tous les éléments.     |
| `ft_lstlast`      | Renvoie le dernier élément de la liste.                                              |
| `ft_lstmap`       | Applique la fonction `f` a chaque element d'une liste pour creer une nouvelle liste. |
| `ft_lstnew`       | Alloue un espace memoire a un nouvel element de liste en precisant son `content`.    |
| `ft_lstsize`      | Compte le nombre d'éléments de la liste.                                             |

---

## Instructions
1. Clonez le depot :
```bash
git clone <https://github.com/42learners/Common-Core---Libft-97125441-174f-47c3-80f1-9bfcdfb06f04.git>
   ```
2. Compilez la bibliotheque :
```bash
make
```
3. Incluez le fichier d'en-tete `libft.h` dans votre projet et liez la bibliotheque lors de la compilation :
```bash
gcc -Wall -Wextra -Werror main.c -L. -lft -o programme
```
4. Pour effacer les fichiers .o et l'executable libft.a :
 ```bash
   make fclean
   ```
---

## Utilisation
Incluez `libft.h` dans votre code et utilisez les fonctions comme suit :
```c
#include "libft.h"

int main(void)
{
    char *str = ft_strdup("Hello, 42!");
    ft_putendl_fd(str, 1);
    free(str);
    return (0);
}
```

---

## Ressources
- La communauté 42;
- gitbook.io;
- stackoverflow.com;

