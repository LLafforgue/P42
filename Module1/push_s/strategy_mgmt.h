/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strategy_mgmt.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:38:13 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 17:23:01 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STRATEGY_MGMT_H
# define STRATEGY_MGMT_H

# include "benchmark.h"

float		compute_disorder_perc(t_stack *stack);
t_e_strat	get_strategy(float disorder_perc, size_t nb_ints);
char		*get_strat_name(t_e_strat strategy);

#endif