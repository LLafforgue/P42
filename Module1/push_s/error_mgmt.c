/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_mgmt.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:12:19 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 14:22:47 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "error_mgmt.h"
#include <unistd.h>

void	clean_exit_with_error(int code, t_stacks *stacks)
{
	write(STDERR_FILENO, "Error\n", 6);
	free_stacks(stacks);
	exit(code);
}

void	free_stacks(t_stacks *stacks)
{
	if (stacks)
	{
		if (stacks->a)
		{
			free(stacks->a->values);
			free(stacks->a->ranks);
			free(stacks->a);
		}
		if (stacks->b)
		{
			free(stacks->b->values);
			free(stacks->b->ranks);
			free(stacks->b);
		}
	}
}
