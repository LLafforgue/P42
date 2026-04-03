/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_index_gen.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 16:00:03 by llafforg          #+#    #+#             */
/*   Updated: 2026/01/07 17:09:02 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	swap(int *values, size_t i, size_t j)
{
	int	temp;

	if (i == j)
		return ;
	temp = values[i];
	values[i] = values[j];
	values[j] = temp;
}

static size_t	partition(int *values, size_t size)
{
	size_t	i;
	size_t	j;

	swap(values, size / 2, size - 1);
	i = 0;
	j = 0;
	while (i < size - 1)
	{
		if (values[i] <= values[size - 1])
			swap(values, i, j++);
		i++;
	}
	swap(values, size - 1, j);
	return (j);
}

static void	quick_sort(int *values, size_t size)
{
	int	pivot;

	if (size < 2)
		return ;
	pivot = partition(values, size);
	quick_sort(values, pivot);
	quick_sort(values + pivot, size - pivot);
}

static void	rank(int *num_ranked, t_stack *a, int i)
{
	t_stack	*temp;

	temp = a;
	while (i >= 0)
	{
		if (num_ranked[i] == a->nbr)
		{
			a->index = i;
			i--;
			a = temp;
		}
		else
			a = a->next;
	}
}

void	ft_set_index(t_stack *a)
{
	int		*num_ranked;
	t_stack	*temp;
	int		i;

	i = 0;
	temp = a;
	num_ranked = malloc(sizeof(int) * ft_lstsize(a));
	if (!num_ranked)
		return ;
	while (a)
	{
		num_ranked[i++] = a->nbr;
		a = a->next;
	}
	quick_sort(num_ranked, ft_lstsize(temp));
	rank(num_ranked, temp, i - 1);
	free(num_ranked);
}
