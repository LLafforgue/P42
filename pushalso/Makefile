# variables:

NAME = push_swap
SRC = main.c list_util.c operations.c operations_bis.c operations_bis_bis.c parse.c utils.c ft_str_utils.c ft_index_gen.c \
		ft_disorder.c list_util_bis.c ft_split.c parse_plus.c bench.c ft_putnbr_fd.c \
		strategy.c algo_simple.c algo_medium.c algo_complex.c algo_medium_utils.c \
		algo_utils.c parse_plus_bis.c
OBJ = ${SRC:%.c=%.o}
CC = cc
CCFLAGS = -Wall -Wextra -Werror -g
N = norminette
RM = rm -f

# rules:

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CCFLAGS) $(OBJ) -o $@ -g
# 	$(N)

%.o: %.c
	$(CC) $(CCFLAGS) -c $< -o $@

clean:
	$(RM) *.o

fclean: clean
	$(RM) $(NAME)

re: fclean all

valgrind: all
	valgrind ./$(NAME) $$(cat args.txt)

.PHONY: all clean fclean re valgrind