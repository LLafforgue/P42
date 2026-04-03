/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 13:06:38 by llafforg          #+#    #+#             */
/*   Updated: 2025/12/01 14:09:30 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

t_pos	ft_eject_atob(t_stacks *stacks, t_pos pos)
{
	size_t	i;

	i = ft_rot_a(stacks, pos);
	pb(stacks);
	return (i);
}

t_pos	ft_eject_btoa(t_stacks *stacks, t_pos pos)
{
	size_t	i;

	i = ft_rot_b(stacks, pos);
	pa(stacks);
	return (i);
}

t_pos	ft_rot_a(t_stacks *stacks, t_pos pos)
{
	t_stack	*a;

	if (pos == 0)
		return (0);
	a = stacks->a;
	if (pos <= a->len / 2)
		while (pos--)
			ra(stacks);
	else
		while (pos++ % a->len)
			rra(stacks);
	return (0);
}

t_pos	ft_rot_b(t_stacks *stacks, t_pos pos)
{
	t_stack	*b;

	if (pos == 0)
		return (0);
	b = stacks->b;
	if (pos <= b->len / 2)
		while (pos--)
			rb(stacks);
	else
		while (pos++ % b->len)
			rrb(stacks);
	return (0);
}
