/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   benchmark.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:38:13 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 17:31:23 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef BENCHMARK_H
# define BENCHMARK_H

# define BENCH "[bench]"

# include "types.h"

void	display_bench(t_stats *stats);
void	compute_stats(t_stacks *stacks, t_args *parsed_args, t_stats *stats);
void	display(t_stacks *stacks);

#endif