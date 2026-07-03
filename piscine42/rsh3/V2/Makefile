#Variables
NAME	= rush-02
SRC	= main.c fts_strs.c ft_parse_all.c ft_split.c ./src/f_rs.c ft_cdu.c
OBJ	= $(SRC:.c=.o)
CFLAGS = -Wall -Wextra -Werror
N = norminette

#regle de base pour construire l'executable
all: $(NAME)
#regle pour construire l'executable a partir des fichiers objets
$(NAME): $(OBJ)
	gcc $(CFLAGS) -o $@ $(OBJ)
# regle pour compiler chaque fichier .c en .o, en incluant rush02.h
%.o: %.c rush_02.h ft_split.h ./lib/rs.h
	gcc $(CFLAGS) -c $< -o $@ 

n:
	$(N)

clean :
	rm -f $(OBJ)
	
fclean : clean
	rm -f $(NAME)
