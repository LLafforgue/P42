/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_complex.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: samlamal <samlamal@student.42.fr>          #+#  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026-02-17 11:15:02 by samlamal          #+#    #+#             */
/*   Updated: 2026-02-17 11:15:02 by samlamal         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//compte le nombres de bit il y a dans 
//dans nombre max de stack
static int	ft_bit(int nbr)
{
	int	byte;

	byte = 0;
	while ((nbr >> byte) > 0)
		byte++;
	return (byte);
}

static void	ft_retrieve(t_data *data)
{
	while (data->len_b)
		ft_push_a(data);
}

//radix
void	algo_complex(t_data *data)
{
	int	i;
	int	bytes;
	int	bit_idx;

	bit_idx = 0;
	if (to_sort(data))
		return ;
	bytes = ft_bit(data->len_a - 1);
	while (bit_idx < bytes)
	{
		i = data->len_a;
		while (i--)
		{
			if (((*data->a)->index >> bit_idx & 1) == 1)
			{
				ft_rotate_up_a(data);
				if (is_sorted(*data->a) && !data->len_b)
					return ;
			}
			else
				ft_push_b(data);
		}
		ft_retrieve(data);
		bit_idx++;
	}
}
