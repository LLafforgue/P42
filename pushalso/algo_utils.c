/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: samlamal <samlamal@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-02-25 12:32:20 by samlamal          #+#    #+#             */
/*   Updated: 2026-02-25 12:32:20 by samlamal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_sorted(t_stack *stack)
{
	if (!stack)
		return (0);
	while (stack->next)
	{
		if (stack->index > stack->next->index)
			return (0);
		stack = stack->next;
	}
	return (1);
}

void	sort_three(t_data *data)
{
	if (is_sorted(*data->a))
		return ;
	while (!is_sorted(*data->a))
	{
		if ((*data->a)->index > (*data->a)->next->index)
			ft_swap_a(data);
		else
			ft_rotate_down_a(data);
	}
}

void	sort_five(t_data *data)
{
	int	idx;
	int	pos;

	idx = 0;
	if (is_sorted(*data->a))
		return ;
	while (data->len_a > 3)
	{
		pos = ft_position(*data->a, idx);
		ft_extract(data, pos);
		idx++;
	}
	sort_three(data);
	ft_push_a(data);
	ft_push_a(data);
}

int	to_sort(t_data *data)
{
	if (data->len_a == 3)
		sort_three(data);
	else if (data->len_a == 5)
		sort_five(data);
	else if (!is_sorted(*data->a))
		return (0);
	return (1);
}
