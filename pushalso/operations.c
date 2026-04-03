/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 17:41:09 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 11:59:45 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_swap_a(t_data *data)
{
	t_stack	*a;
	t_stack	*b;
	t_stack	*c;

	if (!data || !data->a || ft_lstsize(*data->a) < 2)
		return ;
	a = (*data->a);
	b = (*data->a)->next;
	c = (*data->a)->next->next;
	(*data->a) = b;
	(*data->a)->next = a;
	(*data->a)->next->next = c;
	data->sa++;
	write(1, "sa\n", 3);
}

void	ft_swap_b(t_data *data)
{
	t_stack	*a;
	t_stack	*b;
	t_stack	*c;

	if (!data || !data->b || ft_lstsize(*data->b) < 2)
		return ;
	a = (*data->b);
	b = (*data->b)->next;
	c = (*data->b)->next->next;
	(*data->b) = b;
	(*data->b)->next = a;
	(*data->b)->next->next = c;
	data->sb++;
	write(1, "sb\n", 3);
}

void	ft_sswap(t_data *data)
{
	int	tmp;

	if (!data || !data->a || !data->b)
		return ;
	if (ft_lstsize(*data->a) < 2)
		return ;
	tmp = (*data->a)->nbr;
	(*data->a)->nbr = (*data->a)->next->nbr;
	(*data->a)->next->nbr = tmp;
	if (ft_lstsize(*data->b) < 2)
		return ;
	tmp = (*data->b)->nbr;
	(*data->b)->nbr = (*data->b)->next->nbr;
	(*data->b)->next->nbr = tmp;
	data->ss++;
	write(1, "ss\n", 3);
}

void	ft_push_a(t_data *data)
{
	t_stack	*new_head;

	if (!data || !data->a || !data->b)
		return ;
	new_head = (*(data->b))->next;
	ft_lstadd_front(data->a, ft_lstnew((*(data->b))->nbr));
	(*(data->a))->index = (*(data->b))->index;
	free(*(data->b));
	*(data->b) = new_head;
	data->pa++;
	data->len_a++;
	data->len_b--;
	write(1, "pa\n", 3);
}

void	ft_push_b(t_data *data)
{
	t_stack	*new_head;

	if (!data || !data->a || !data->b)
		return ;
	new_head = (*(data->a))->next;
	ft_lstadd_front(data->b, ft_lstnew((*(data->a))->nbr));
	(*(data->b))->index = (*(data->a))->index;
	free(*(data->a));
	*(data->a) = new_head;
	data->pb++;
	data->len_a--;
	data->len_b++;
	write(1, "pb\n", 3);
}
