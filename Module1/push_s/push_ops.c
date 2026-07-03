/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_ops.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:51:34 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 18:09:16 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operations.h"
#include "ft_printf.h"
#include "shift_ops.h"

static void	push(t_stack *stack, int value, unsigned int rank)
{
	stack->len++;
	ft_shift_down(stack);
	stack->values[0] = value;
	stack->ranks[0] = rank;
}

static void	pop(t_stack *stack, int *popped_value, unsigned int *popped_rank)
{
	*popped_value = stack->values[0];
	*popped_rank = stack->ranks[0];
	ft_shift_up(stack);
	stack->len--;
}

void	pa(t_stacks *stacks)
{
	int				value;
	unsigned int	rank;

	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[PA]++;
	if (stacks->b->len)
	{
		pop(stacks->b, &value, &rank);
		push(stacks->a, value, rank);
	}
}

void	pb(t_stacks *stacks)
{
	int				value;
	unsigned int	rank;

	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[PB]++;
	if (stacks->a->len)
	{
		pop(stacks->a, &value, &rank);
		push(stacks->b, value, rank);
	}
}
