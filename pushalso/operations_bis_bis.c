/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_bis_bis.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/26 14:18:19 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 11:54:24 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	rote_d(t_stack **stack)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	first = *stack;
	while (first->next->next)
		first = first->next;
	end = first->next;
	tmp = first;
	first = *stack;
	end->next = first;
	*stack = end;
	tmp->next = NULL;
}

void	ft_rrrotate_down(t_data *data)
{
	if (!data || !data->a || !data->b
		|| !*(data->a) || !*(data->b)
		|| !(*(data->a))->next
		|| !(*(data->b))->next)
		return ;
	rote_d(data->a);
	rote_d(data->b);
	data->rrr += 1;
	write(1, "rrr\n", 4);
}
