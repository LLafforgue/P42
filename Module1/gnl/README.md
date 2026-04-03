*This project has been created as part of the 42 curriculum by llafforg*

[![42](https://img.shields.io/badge/42-Project-blue)](https://www.42.fr/)

# get_next_line

---

## Table des matieres
- [Description](#description)
    - [Fonctions](#fonctions)
    - [Variables](#variables)
- [Instructions](#instructions)
- [Utilisation](#instructions)
- [Algroithme](#algorithme)
- [Ressources](#ressources)

---

## Description
**get_next_line** est une fonction qui permet de lire le fichier ouvert sur une `fd` predefinie et de renvoyer a chaque appel la chaine de caractere d'une ligne entiere avec le renvoi a la ligne associe.
En cas d'erreur ou de fichier entierement lu, la fonction renvoi un pointeur nul.
La bibliotheque `get_next_line.h` permet d'acceder aux elements suivants :

### Fonctions

| Fonction          | Description                                                      |
|-------------------|------------------------------------------------------------------|
| `ft_calloc_empty` | Alloue un tableau de taille `size_t size` en memoire heap.       |
| `ft_chek_line`    | Verifie qu'une string contient le `SEPARATOR`.                   |
| `ft_error`        | Free un espace memoire et retourne NULL.                         |
| `ft_strlen`       | Mesure la taille d'une chaine de caractere finissant par '\0'    |
| `get_next_line`   | Renvoie la ligne lue dans un fichier ouvert sur `fd`.            |

### Variables

| Variables     | Valeur | Description                                                        |
|---------------|--------|--------------------------------------------------------------------|
| `BUFFER_SIZE` | 42     | Taille de lecture sur `fd`.                                        |
| `SEPARATOR`   | '\n'   | Delimite (char) la chaine caracteres de retour de `get_next_line`. |


---

## Instructions
1. Clonez le depot :
```bash
git clone <https://github.com/42learners/Common-Core---GetNextLine-aab999c6-14e4-4d61-8c28-92f90e11a96a.git>
   ```
2. Compilez avec un main (non fournit):
```bash
cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c get_next_line.h <votre main>.c
```

## Utilisation
Exemple de main
```c
#include "get_next_line.h"

int	main(void)
{
	int		fd;
	int		cnt;
	int		deb;
	char	*line;

	deb = 0;
	cnt = 15;
	fd = open("<votre fichier>", O_RDONLY);
	while (deb < cnt)
	{
		line = get_next_line(fd);
		printf("l%d : %s-----\n", deb + 1, line);
		deb++;
		free(line);
	}
	close(fd);
} 

```

---

## Algorithme
get_next_line a un algorithme construit en 4 phases autour d'un principe de base qui est de construitre via une boucle conditionnee, une chaine de caracteres qui contiendra le *SEPARATOR* pour stopper la chaine. Les quatres phases sont :
- 1/ <font color="blue">Initialisation - Recuperation</font>
- 2/ <font color="blue">Lecture</font>
- 3/ <font color="blue">Concatenation</font>
- 4/ <font color="blue">Verifications - Erreurs</font>

**Initialisation - Recuperation** initialise la chaine de caracteres vide (*str*). La taille de lecture du fichier demarre a 0 est reste en memoire apres chaque appel (*read_size*). Il en va de meme pour le buffer (chaine de caracteres) qui recupere les caracteres lus (*buff*). La position du caractere suivant le dernier lu dans ce buffer est aussi enregistre (*i*).\
La **lecture** sur *fd* permet de remplir *buff*. Elle se fait uniquement si *i < read_size*.\
La **concatenation** de *str* et *buff* se fait jusqu'a la fin de *buff* si aucun *SEPARATOR* n'est identifier dans *buff*.\
Les **verifications** identifient si le document et lu en entier, tout le *buff* a ete concatene et teste, si la lecture sur le *fd* a rate. Les **erreurs** assurent la liberation de la memoire allouee.

---

## Ressources
- La communauté 42;
- gitbook.io;
- stackoverflow.com;
- https://github.com/Tripouille;

