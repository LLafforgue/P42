/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   quick_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:30:59 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 18:32:43 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"
#include "types.h"

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

void	quick_sort(int *values, size_t size)
{
	int	pivot;

	if (size < 2)
		return ;
	pivot = partition(values, size);
	quick_sort(values, pivot);
	quick_sort(values + pivot, size - pivot);
}
