/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_plus_bis.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/27 15:23:54 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 15:23:56 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_check_stack(t_stack **a, t_errors *errors)
{
	if (!(*a))
	{
		errors->error_no_stack = 1;
		ft_display_errors(*errors);
		return (1);
	}
	if (errors->error_duplicate || errors->error_max)
	{
		ft_display_errors(*errors);
		ft_lstclear(a);
		return (1);
	}
	return (0);
}
