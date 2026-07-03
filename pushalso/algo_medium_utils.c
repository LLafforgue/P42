/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_medium_utils.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: samlamal <samlamal@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-02-24 13:04:54 by samlamal          #+#    #+#             */
/*   Updated: 2026-02-24 13:04:54 by samlamal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	bucket_in_stack(t_stack *stack, int bucket, int bucket_size)
{
	int	index_buket;

	if (!stack)
		return (0);
	while (stack)
	{
		index_buket = stack->index / bucket_size;
		if (index_buket == bucket)
			return (1);
		stack = stack->next;
	}
	return (0);
}

int	ft_sqrt(int n)
{
	int	start;
	int	end;
	int	rslt;
	int	middle;

	start = 1;
	end = n;
	rslt = 0;
	if (n < 0)
		return (-1);
	if ((n == 0) || n == 1)
		return (n);
	while (start <= end)
	{
		middle = start + (end - start) / 2;
		if (middle <= n / middle)
		{
			rslt = middle;
			start = middle + 1;
		}
		else
			end = middle - 1;
	}
	return (rslt);
}
