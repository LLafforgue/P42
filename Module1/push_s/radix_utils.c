/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 13:06:38 by llafforg          #+#    #+#             */
/*   Updated: 2025/12/01 14:40:29 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

unsigned int	ft_max_digits(unsigned int *numbers, size_t size)
{
	int				max;
	unsigned int	digits;

	max = numbers[ft_search_max(numbers, size)];
	digits = 0;
	while (max > 0)
	{
		max /= RADIX;
		digits++;
	}
	return (digits);
}

unsigned int	ft_pow(unsigned int radix, int exponent)
{
	if (radix == 0 || exponent == 1)
		return (radix);
	if (exponent <= 0)
		return (1);
	if (exponent > 1)
		return (radix * ft_pow(radix, exponent - 1));
	return (0);
}

bool	ft_is_ascending(unsigned int *numbers, size_t size)
{
	t_pos	i;

	i = 0;
	while (i < size - 1)
	{
		if (numbers[i] > numbers[i + 1])
			return (false);
		i++;
	}
	return (true);
}

t_pos	ft_search_max(unsigned int *numbers, size_t size)
{
	t_pos	i;
	t_pos	i_max;

	i = 1;
	i_max = 0;
	while (i < size)
	{
		if (numbers[i] > numbers[i_max])
			i_max = i;
		i++;
	}
	return (i_max);
}
