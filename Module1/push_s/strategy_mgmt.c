/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strategy_mgmt.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 17:16:42 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 18:24:09 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "strategy_mgmt.h"
#include "benchmark.h"

char	*get_strat_name(t_e_strat strategy)
{
	if (strategy == SIMPLE)
		return ("O(n²)");
	if (strategy == MEDIUM)
		return ("O(n\xE2\x88\x9An)");
	if (strategy == COMPLEX)
		return ("O(n log(n))");
	return ("?");
}

float	compute_disorder_perc(t_stack *stack)
{
	size_t	i;
	size_t	j;
	int		pairs;
	int		unordered;

	i = 0;
	pairs = 0;
	unordered = 0;
	while (i < stack->len - 1)
	{
		j = i + 1;
		while (j < stack->len)
		{
			if (stack->values[i] > stack->values[j])
				unordered++;
			pairs++;
			j++;
		}
		i++;
	}
	return (100.0f * unordered / pairs);
}

t_e_strat	get_strategy(float disorder_perc, size_t nb_ints)
{
	if (disorder_perc < 20.0f || nb_ints < 20)
		return (SIMPLE);
	if (disorder_perc < 50.0f)
		return (MEDIUM);
	return (COMPLEX);
}
