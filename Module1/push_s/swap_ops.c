/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:47:14 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/27 18:59:03 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operations.h"
#include "ft_printf.h"

static void	swap(t_stack *stack)
{
	int				top_value;
	unsigned int	top_rank;

	if (stack->len < 2)
		return ;
	top_value = stack->values[0];
	top_rank = stack->ranks[0];
	stack->values[0] = stack->values[1];
	stack->ranks[0] = stack->values[1];
	stack->values[1] = top_value;
	stack->ranks[1] = top_rank;
}

void	sa(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[SA]++;
	swap(stacks->a);
}

void	sb(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[SB]++;
	swap(stacks->b);
}

void	ss(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[SS]++;
	swap(stacks->a);
	swap(stacks->b);
}
