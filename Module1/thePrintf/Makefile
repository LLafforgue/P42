#Variables
NAME = libftprintf.a
SRC = ft_printf.c ft_put_str.c ft_put_nbr.c ft_put_address.c ft_put_unsigned_hex.c ft_put_unsigned_nbr.c
AR = ar rcs
OBJ = $(SRC:%.c=%.o)
N = norminette
CFLAG = -Werror -Wall -Wextra

#regles
all : $(NAME) 

$(NAME) : $(OBJ)
	$(AR) $(NAME) $(OBJ)

%.o : %.c ft_printf.h
	gcc $(CFLAG) -c $< -o $@

clean :
	rm -f $(OBJ)

fclean : clean
	rm -f $(NAME)

re : fclean all

n :
	$(N)
