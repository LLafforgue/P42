/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_algo.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 17:40:25 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 12:01:17 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_position(t_stack *stack, int idx)
{
	int	i;

	i = 0;
	if (!stack)
		return (-1);
	while (stack)
	{
		if (stack->index == idx)
			return (i);
		i++;
		stack = stack->next;
	}
	return (-1);
}

void	ft_extract(t_data *data, int pos)
{
	if (pos <= data->len_a / 2)
	{
		while (pos > 0)
		{
			ft_rotate_up_a(data);
			pos--;
		}
	}
	else
	{
		while (pos < data->len_a)
		{
			ft_rotate_down_a(data);
			pos++;
		}
	}
	ft_push_b(data);
}

//min extraction method
void	simple_algo(t_data *data)
{
	int	i;
	int	len;
	int	pos;

	i = 0;
	pos = 0;
	len = data->len_a;
	if (to_sort(data))
		return ;
	while (i < len - 1)
	{
		pos = ft_position(*(data->a), i);
		if (pos != -1)
			ft_extract(data, pos);
		if (is_sorted(*data->a) && data->len_b == 0)
			return ;
		i++;
	}
	while (data->len_b)
		ft_push_a(data);
}
