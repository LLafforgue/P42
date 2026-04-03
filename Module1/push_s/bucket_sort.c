/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bucket_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:56:19 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/28 17:55:38 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

static unsigned int	ft_sqrt(unsigned int n)
{
	unsigned int	sqrt;

	sqrt = 1;
	while (sqrt * sqrt <= n)
		sqrt++;
	return (sqrt - 1);
}

static void	ft_range_bucket(t_stacks *stacks, unsigned int max_in_bucket)
{
	t_stack	*a;
	size_t	pos;

	a = stacks->a;
	pos = 0;
	while (pos < a->len)
	{
		if (a->ranks[pos] < max_in_bucket)
			pos = ft_eject_atob(stacks, pos);
		else
			pos++;
	}
}

static void	ft_max_extraction_b(t_stacks *stacks)
{
	size_t	pos;

	while (stacks->b->len)
	{
		pos = ft_search_max(stacks->b->ranks, stacks->b->len);
		ft_eject_btoa(stacks, pos);
	}
}

void	bucket_sort(t_stacks *stacks)
{
	size_t			n;
	unsigned int	n_buckets;
	unsigned int	current_bucket;
	unsigned int	max_in_bucket;

	n = stacks->a->len;
	n_buckets = ft_sqrt(n);
	current_bucket = 1;
	while (current_bucket < n_buckets)
	{
		max_in_bucket = current_bucket * n / n_buckets;
		ft_range_bucket(stacks, max_in_bucket);
		current_bucket++;
	}
	min_extract_sort(stacks);
	ft_max_extraction_b(stacks);
}
