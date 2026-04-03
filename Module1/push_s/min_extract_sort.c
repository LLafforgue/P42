/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   min_extract_sort.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 13:06:33 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/28 18:00:02 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

static size_t	ft_search_min(unsigned int *a, int size)
{
	int		i;
	size_t	pos;

	i = 1;
	pos = 0;
	while (i < size)
	{
		while (a[i] > a[pos] && i < size)
			i++;
		if (i == size && a[i - 1] > a[pos])
			return (pos);
		pos = i;
		i++;
	}
	return (pos);
}

static int	ft_sorted_ra(unsigned int *a, int len)
{
	int	base;
	int	i;
	int	j;
	int	n_num;

	if (len == 1)
		return (1);
	if (!len)
		return (0);
	i = ft_search_min(a, len);
	j = (i + 1) % len;
	base = a[i] > a[j];
	n_num = 1;
	while (n_num < len - 1)
	{
		i = (i + 1) % len;
		j = (i + 1) % len;
		if (base != (a[i] > a[j]))
			return (0);
		n_num++;
	}
	return (1);
}

void	min_extract_sort(t_stacks *stacks)
{
	size_t	pos;
	size_t	total_len;

	total_len = stacks->a->len;
	while (!ft_is_ascending(stacks->a->ranks, stacks->a->len))
	{
		pos = ft_search_min(stacks->a->ranks, stacks->a->len);
		ft_eject_atob(stacks, pos);
		if (ft_sorted_ra(stacks->a->ranks, stacks->a->len))
			ft_rot_a(stacks, ft_search_min(stacks->a->ranks, stacks->a->len));
	}
	while (stacks->a->len < total_len)
		pa(stacks);
}
