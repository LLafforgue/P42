/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_bis.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 18:00:29 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 11:59:09 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//ra: first element of stack become last
void	ft_rotate_up_a(t_data *data)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	if (!data || ft_lstsize(*(data->a)) < 2)
		return ;
	first = *(data->a);
	end = *(data->a);
	while (end->next)
		end = end->next;
	tmp = first->next;
	end->next = first;
	first->next = NULL;
	*(data->a) = tmp;
	data->ra += 1;
	write(1, "ra\n", 3);
}

//rb: first element of stack become last
void	ft_rotate_up_b(t_data *data)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	if (!data || ft_lstsize(*(data->b)) < 2)
		return ;
	first = *(data->b);
	end = *(data->b);
	while (end->next)
		end = end->next;
	tmp = first->next;
	end->next = first;
	first->next = NULL;
	*(data->b) = tmp;
	data->rb += 1;
	write(1, "rb\n", 3);
}

//rr: ra & rb en meme temps
void	ft_rrotate_up(t_data *data)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	if (!data || ft_lstsize(*(data->a)) < 2 || ft_lstsize(*(data->b)) < 2)
		return ;
	first = *(data->a);
	end = *(data->a);
	while (end->next)
		end = end->next;
	tmp = first->next;
	end->next = first;
	first->next = NULL;
	*(data->a) = tmp;
	first = *(data->b);
	end = *(data->b);
	while (end->next)
		end = end->next;
	tmp = first->next;
	end->next = first;
	first->next = NULL;
	*(data->b) = tmp;
	data->rr += 1;
	write(1, "rr\n", 3);
}

void	ft_rotate_down_a(t_data *data)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	if (!data || ft_lstsize(*(data->a)) < 2)
		return ;
	first = *(data->a);
	while (first->next->next)
		first = first->next;
	end = first->next;
	tmp = first;
	first = *(data->a);
	end->next = first;
	*(data->a) = end;
	tmp->next = NULL;
	data->rra += 1;
	write(1, "rra\n", 4);
}

void	ft_rotate_down_b(t_data *data)
{
	t_stack	*first;
	t_stack	*end;
	t_stack	*tmp;

	if (!data || ft_lstsize(*(data->b)) < 2)
		return ;
	first = *(data->b);
	while (first->next->next)
		first = first->next;
	end = first->next;
	tmp = first;
	first = *(data->b);
	end->next = first;
	*(data->b) = end;
	tmp->next = NULL;
	data->rrb += 1;
	write(1, "rrb\n", 4);
}
