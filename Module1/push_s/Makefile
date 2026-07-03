# variables:

NAME = push_swap
SRC = push_swap.c \
		args_parser.c benchmark.c error_mgmt.c \
		ft_atoi.c ft_bzero.c ft_calloc.c ft_format_char.c ft_format_double.c \
		ft_format_hex.c ft_format_ptr.c ft_format_signed.c ft_format_string.c \
		ft_format_unsigned.c ft_isalpha.c ft_isdigit.c \
		ft_itoa.c ft_memcpy.c ft_memset.c ft_printf.c ft_putchar_fd.c \
		ft_putstr_fd.c ft_strchr.c ft_strjoin.c ft_strlen.c ft_strncmp.c \
		push_ops.c quick_sort.c rev_rotate_ops.c rotate_ops.c shift_ops.c \
		stack_mgmt.c strategy_mgmt.c swap_ops.c \
		bucket_sort.c min_extract_sort.c radix_sort.c  radix_utils.c sort_utils.c

OBJ = ${SRC:%.c=%.o}

CC = cc
CCFLAGS = -Wall -Wextra -Werror
N = norminette -R CheckForbiddenSourceHeader -R CheckDefine
RM = rm -f

# rules:

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CCFLAGS) $(OBJ) -o $@
	$(N)

%.o: %.c
	$(CC) $(CCFLAGS) -c $< -o $@

clean:
	$(RM) *.o

fclean: clean
	$(RM) $(NAME)

re: fclean all

run: all
	./$(NAME) $$(cat args.txt)

bench: all
	./$(NAME) $$(cat args.txt) --bench

test: all
	./$(NAME) $$(cat args.txt) --bench | ./checker_os $$(cat args.txt)

valgrind: all
	valgrind ./$(NAME) $$(cat args.txt)

.PHONY: all clean fclean re run bench test valgrind