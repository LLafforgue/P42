/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 13:55:06 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 15:23:17 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>

typedef struct s_stack
{
	int				nbr;
	int				index;
	struct s_stack	*next;
}					t_stack;

typedef struct s_data
{
	t_stack	**a;
	t_stack	**b;
	int		len_a;
	int		len_b;
	int		sa;
	int		sb;
	int		ra;
	int		rb;
	int		rr;
	int		rra;
	int		rrb;
	int		rrr;
	int		ss;
	int		pa;
	int		pb;

	float	disorder;
}			t_data;

typedef struct s_args
{
	int	flag_bench;
	int	flag_simple;
	int	flag_medium;
	int	flag_complex;
	int	flag_adaptive;

}			t_args;

typedef struct s_errors
{
	int	error_strategy;
	int	error_args;
	int	error_no_stack;
	int	error_duplicate;
	int	error_max;
}			t_errors;

// --- CHECK & PARSE
int		ft_check_parse(char **arg, t_stack **a, t_args *args, t_errors *errors);
float	ft_disorder(t_data	*data);
void	ft_put_disorder(int fd, float dis);
void	ft_set_index(t_stack *a);
int		parse_splited(char *arg, t_stack **a, t_args *args, t_errors *errors);
int		is_valid(char *str, t_args *args, t_errors *errors);
void	print_bench(int fd, t_data *data, t_args args);
void	set_strategy(t_args *args, t_data *data);
void	init_flags(t_args *args, t_errors *errors);
int		ft_check_stack(t_stack **a, t_errors *errors);
void	ft_display_errors(t_errors errors);
void	ft_put_nbr_stack(char *str, t_stack **a, t_errors *errors);
int		ft_check_stack(t_stack **a, t_errors *errors);

//	--- UTILS
void	ft_putstr(char *str, int fd);
char	*ft_itoa(int nbr);
int		ft_atoi(char *str);
int		ft_power(int pwd, int exp);
void	ft_putnbr_fd(int fd, int n);

// ---- LST_UTILS
t_stack	*ft_lstnew(int nbr);
int		ft_lstsize(t_stack *stack);
void	ft_lstprint(t_stack *stack);
void	ft_lstadd_front(t_stack **lst, t_stack *new);
void	ft_lstadd_back(t_stack **stack, t_stack *new);
void	ft_lstclear(t_stack **stack);
void	ft_lstprint_index(t_stack *stack);

// ---- OPERATIONS
void	ft_swap_a(t_data *data);	// sa
void	ft_swap_b(t_data *data);	// sb
void	ft_sswap(t_data *data);				// ss
void	ft_push_a(t_data *data);			// pa
void	ft_push_b(t_data *data);			// pb
void	ft_rotate_up_a(t_data *data);		// ra
void	ft_rotate_up_b(t_data *data);		// rb
void	ft_rrotate_up(t_data *data);		// rr
void	ft_rotate_down_a(t_data *data);		// rra
void	ft_rotate_down_b(t_data *data);		// rrb
void	ft_rrrotate_down(t_data *data);		// rrr

// ---- STR
int		ft_strncmp(const char *s1, const char *s2, size_t n);
char	**ft_split(const char *s, char c);

// --- SORT
void	simple_algo(t_data *data);
void	medium_algo(t_data *data);
int		ft_position(t_stack *stack, int idx);
void	algo_complex(t_data *data);
int		is_sorted(t_stack *stack);
int		bucket_in_stack(t_stack *stack, int bucket, int bucket_size);
int		ft_sqrt(int n);
void	sort_three(t_data *data);
void	ft_extract(t_data *data, int pos);
int		to_sort(t_data *data);

#endif
