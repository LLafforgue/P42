/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_rotate_ops.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:44:19 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/25 16:29:15 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "types.h"
#include "ft_printf.h"
#include "shift_ops.h"

void	rra(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RRA]++;
	ft_shift_down(stacks->a);
}

void	rrb(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RRB]++;
	ft_shift_down(stacks->b);
}

void	rrr(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RRR]++;
	ft_shift_down(stacks->a);
	ft_shift_down(stacks->b);
}
