/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_medium.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 18:13:20 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/13 13:30:04 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	ft_push_b_perf(t_data *data)
{
	int		x_index;
	t_stack	*n_index;

	x_index = (*data->a)->index;
	ft_push_b(data);
	n_index = (*data->b)->next;
	if (n_index && n_index->index > x_index)
		ft_swap_b(data);
}

//Max extraction
static void	ft_extract_b(t_data *data, int pos)
{
	if (pos == 0)
	{
		ft_push_a(data);
		return ;
	}
	else if (pos < data->len_b / 2)
	{
		while (pos > 0)
		{
			ft_rotate_up_b(data);
			pos--;
		}
	}
	else if (pos >= data->len_b / 2)
	{
		while (pos < data->len_b)
		{
			ft_rotate_down_b(data);
			pos++;
		}
	}
	ft_push_a(data);
}

//simple algo
static void	ft_sort(t_data *data)
{
	int	pos;
	int	index;

	pos = 0;
	index = data->len_b - 1;
	while (data->len_b)
	{
		pos = ft_position(*data->b, index);
		ft_extract_b(data, pos);
		index--;
	}
}

void	medium_algo(t_data *data)
{
	int	i;
	int	nbr_bucket;
	int	index_bucket;

	i = 0;
	nbr_bucket = ft_sqrt(data->len_a);
	if (to_sort(data))
		return ;
	while (data->len_a)
	{
		index_bucket = (*data->a)->index / nbr_bucket;
		if (index_bucket == i)
			ft_push_b_perf(data);
		else
			ft_rotate_up_a(data);
		if (!bucket_in_stack((*data->a), i, nbr_bucket))
			i++;
	}
	ft_sort(data);
}
