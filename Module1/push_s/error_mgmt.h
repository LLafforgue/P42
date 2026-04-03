/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_mgmt.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 13:14:29 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 13:29:13 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef ERROR_MGMT_H
# define ERROR_MGMT_H

# define INVALID_NUM_ERROR 1
# define DUPLICATE_NUM_ERROR 2
# define INVALID_ARG_ERROR 5
# define INCONSISTENT_ARGS_ERROR 6
# define MALLOC_ERROR 10

# include "types.h"

void	clean_exit_with_error(int code, t_stacks *stacks);
void	free_stacks(t_stacks *stacks);

#endif