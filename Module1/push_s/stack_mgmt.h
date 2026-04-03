/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_mgmt.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 16:29:38 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 17:31:43 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STACK_MGMT_H
# define STACK_MGMT_H

# include "types.h"

bool	init_stacks(t_stacks *stacks, size_t size);
void	fill_stack_a(int count, char **args, t_stacks *stacks);

#endif