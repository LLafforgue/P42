/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_disorder.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 11:07:07 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 14:46:43 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//Faire un put_nbr pour float + appeler la fonction pour adaptive/std strategy
//appeler la foncttion pour affichage Bench
float	ft_disorder(t_data *data)
{
	int		mistake;
	int		paires;
	t_stack	*a_stack;

	if (data->len_a == 1)
	{
		data->disorder = 0;
		return (data->disorder);
	}
	a_stack = *(data->a);
	mistake = 0;
	paires = 0;
	while (a_stack->next)
	{
		if (a_stack->index > a_stack->next->index)
			mistake += 1;
		paires += 1;
		a_stack = a_stack->next;
	}
	data->disorder = 100 * mistake / paires;
	return (data->disorder);
}

int	ft_power(int pwd, int exp)
{
	if (pwd <= 0)
		return (0);
	if (exp == 0)
		return (1);
	if (exp < 0)
		return (0);
	if (exp == 1)
		return (pwd);
	return (pwd * ft_power(pwd, exp - 1));
}

static void	ft_print_dis_number(int fd, int number)
{
	int		i;
	int		exp;
	char	dis_put;

	i = 5;
	exp = 3;
	while (i > 0)
	{
		if (i == 3)
		{
			dis_put = '.';
			write(fd, &dis_put, 1);
		}
		else
		{
			dis_put = (number / ft_power(10, exp)) + '0';
			write(fd, &dis_put, 1);
			number = number % ft_power(10, exp--);
		}
		i--;
	}
}

void	ft_put_disorder(int fd, float dis)
{
	int		dis_int;

	dis_int = (int)(dis * 100);
	if (dis_int == 10000)
	{
		write(fd, "100.00%\n", 8);
		return ;
	}
	ft_print_dis_number(fd, dis_int);
	write(fd, "%\n", 2);
}
