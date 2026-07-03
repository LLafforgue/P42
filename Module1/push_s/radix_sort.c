/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radix_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 13:06:42 by llafforg          #+#    #+#             */
/*   Updated: 2025/12/01 14:56:10 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"
#include "types.h"

static int	ft_search_digit_max(unsigned int *numbers, size_t size,
	t_pos nth_digit, unsigned int d)
{
	t_pos			i;
	t_pos			i_max;
	unsigned int	power;

	power = ft_pow(RADIX, (int)nth_digit);
	i_max = 0;
	i = 1;
	while (i < size)
	{
		if ((numbers[i] / power) % RADIX == d
			&& numbers[i] % power > numbers[i_max] % power)
			i_max = i;
		i++;
	}
	return (i_max);
}

static int	ft_search_digit_min(unsigned int *numbers, size_t size,
	t_pos nth_digit, unsigned int d)
{
	t_pos			i;
	t_pos			i_min;
	unsigned int	power;

	power = ft_pow(RADIX, nth_digit);
	i_min = 0;
	i = 1;
	while (i < size)
	{
		if ((numbers[i] / power) % RADIX == d
			&& numbers[i] % power < numbers[i_min] % power)
			i_min = i;
		i++;
	}
	return (i_min);
}

static void	ft_radix_even_atob(t_stacks *stacks, int nth_digit)
{
	t_pos			i;
	t_stack			*a;
	unsigned int	d;
	unsigned int	power;

	power = ft_pow(RADIX, nth_digit);
	d = 0;
	a = stacks->a;
	i = 0;
	while (d < RADIX && a->len)
	{
		while (a->len && i < a->len)
		{
			if ((a->ranks[i] / power) % RADIX == d)
				i = ft_eject_atob(stacks, i);
			else
				i++;
		}
		d++;
		i = ft_search_digit_min(a->ranks, a->len, nth_digit, d);
		i = ft_rot_a(stacks, i);
	}
}

static void	ft_radix_odd_btoa(t_stacks *stacks, int nth_digit)
{
	t_pos			i;
	t_stack			*b;
	unsigned int	d;
	unsigned int	power;

	i = 0;
	d = RADIX;
	power = ft_pow(RADIX, nth_digit);
	b = stacks->b;
	while (d > 0 && b->len)
	{
		while (i < b->len)
		{
			if ((b->ranks[i] / power) % RADIX == d - 1
				&& b->ranks[i] > power - 1)
				i = ft_eject_btoa(stacks, i);
			else
				i++;
		}
		d--;
		i = ft_search_digit_max(b->ranks, b->len, nth_digit, d - 1);
		i = ft_rot_b(stacks, i);
	}
	nth_digit = ft_search_max(b->ranks, b->len);
	ft_rot_b(stacks, nth_digit);
}

void	radix_sort(t_stacks *stacks)
{
	unsigned int	nth_digit;
	unsigned int	last_digit;
	t_stack			*a;
	t_stack			*b;

	nth_digit = 0;
	a = stacks->a;
	b = stacks->b;
	last_digit = ft_max_digits(a->ranks, a->len);
	while (!ft_is_ascending(a->ranks, a->len) && nth_digit <= last_digit)
	{
		if (nth_digit % 2 == 0)
			ft_radix_even_atob(stacks, nth_digit);
		else
			ft_radix_odd_btoa(stacks, nth_digit);
		nth_digit++;
	}
	nth_digit = ft_search_max(b->ranks, b->len);
	ft_rot_b(stacks, nth_digit);
	while (b->len)
		pa(stacks);
}
