/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_plus.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 13:45:05 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 17:22:23 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_check_digit_args(char *str, t_stack **a, t_errors *errors)
{
	t_stack	*tmp;

	if (ft_atoi(str) == 2147483647)
	{
		errors->error_max = 1;
		return (1);
	}
	tmp = *a;
	while (tmp)
	{
		if (tmp->nbr == ft_atoi(str))
		{
			errors->error_duplicate = tmp->nbr;
			return (1);
		}
		tmp = tmp->next;
	}
	return (0);
}

void	ft_put_nbr_stack(char *str, t_stack **a, t_errors *errors)
{
	int		i;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return ;
		i++;
	}
	if (ft_check_digit_args(str, a, errors))
		return ;
	ft_lstadd_back(a, ft_lstnew(ft_atoi(str)));
}

static void	ft_free(char **split)
{
	while (split)
		free(*split++);
	free(split);
}

int	parse_splited(char *arg, t_stack **a, t_args *args, t_errors *errors)
{
	char	**splited;
	char	**temp;

	splited = ft_split(arg, ' ');
	if (!splited)
		return (0);
	temp = splited;
	while (*splited)
	{
		if (!*splited || !is_valid(*splited, args, errors))
		{
			ft_free(splited);
			return (0);
		}
		ft_put_nbr_stack(*splited, a, errors);
		free(*splited++);
	}
	free(temp);
	return (1);
}

void	init_flags(t_args *args, t_errors *errors)
{
	args->flag_bench = 0;
	args->flag_simple = 0;
	args->flag_medium = 0;
	args->flag_complex = 0;
	args->flag_adaptive = 0;
	errors->error_args = 0;
	errors->error_strategy = 0;
	errors->error_no_stack = 0;
	errors->error_duplicate = 0;
}
