/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   shift_ops.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:48:52 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/27 18:24:16 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "shift_ops.h"
#include "types.h"

void	ft_shift_up(t_stack *stack)
{
	int				top;
	unsigned int	top_rank;
	size_t			i;

	if (stack->len < 2)
		return ;
	top = stack->values[0];
	top_rank = stack->ranks[0];
	i = 0;
	while (++i < stack->len)
	{
		stack->values[i - 1] = stack->values[i];
		stack->ranks[i - 1] = stack->ranks[i];
	}
	stack->values[stack->len - 1] = top;
	stack->ranks[stack->len - 1] = top_rank;
}

void	ft_shift_down(t_stack *stack)
{
	int				bottom;
	unsigned int	bottom_rank;
	size_t			i;

	if (stack->len < 2)
		return ;
	i = stack->len;
	bottom = stack->values[i - 1];
	bottom_rank = stack->ranks[i - 1];
	while (--i > 0)
	{
		stack->values[i] = stack->values[i - 1];
		stack->ranks[i] = stack->ranks[i - 1];
	}
	stack->values[0] = bottom;
	stack->ranks[0] = bottom_rank;
}
