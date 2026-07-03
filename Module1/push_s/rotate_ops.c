/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate_ops.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:40:38 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/27 17:10:16 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operations.h"
#include "ft_printf.h"
#include "shift_ops.h"

void	ra(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RA]++;
	ft_shift_up(stacks->a);
}

void	rb(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RB]++;
	ft_shift_up(stacks->b);
}

void	rr(t_stacks *stacks)
{
	ft_printf("%s\n", __func__);
	stacks->stats->op_calls[RR]++;
	ft_shift_up(stacks->a);
	ft_shift_up(stacks->b);
}
