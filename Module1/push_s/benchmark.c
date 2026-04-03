/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   benchmark.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:37:32 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 17:31:23 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "benchmark.h"
#include "strategy_mgmt.h"
#include "ft_printf.h"

static unsigned int	ft_sum_unsigned(unsigned int values[], size_t n)
{
	size_t			i;
	unsigned int	sum;

	sum = 0;
	i = 0;
	while (i < n)
		sum += values[i++];
	return (sum);
}

static void	reset_op_stats(t_stats *stats)
{
	size_t	i;

	stats->total_ops = 0;
	i = 0;
	while (i < OPS_END)
		stats->op_calls[i++] = 0;
}

void	display_bench(t_stats *stats)
{
	unsigned int	*ops;

	ft_printf_err(BENCH " n:\t\t%u\n",
		stats->nb_ints);
	ft_printf_err(BENCH " disorder:\t%f%%\n", stats->disorder_perc);
	if (stats->is_adaptive)
		ft_printf_err(BENCH " strategy:\tAdaptive / %s\n",
			get_strat_name(stats->actual_strategy));
	else
		ft_printf_err(BENCH " strategy:\t%s\n",
			get_strat_name(stats->actual_strategy));
	ops = stats->op_calls;
	stats->total_ops = ft_sum_unsigned(ops, OPS_END);
	ft_printf_err(BENCH " total ops:\t%i\n", stats->total_ops);
	ft_printf_err(BENCH " sa: %u\tsb: %u\tss: %u\tpa: %u\tpb: %u\n",
		ops[SA], ops[SB], ops[SS], ops[PA], ops[PB]);
	ft_printf_err(BENCH " ra: %u\trb: %u\trr: %u\trra: %u\trrb: %u\trrr: %u\n",
		ops[RA], ops[RB], ops[RR], ops[RRA], ops[RRB], ops[RRR]);
}

void	display(t_stacks *stacks)
{
	size_t	i;

	ft_printf_err("A:\n");
	i = 0;
	while (i < stacks->a->len)
	{
		ft_printf_err("[%i] (%u)\n", stacks->a->values[i], stacks->a->ranks[i]);
		i++;
	}
	ft_printf_err("B:\n");
	i = 0;
	while (i < stacks->b->len)
	{
		ft_printf_err("[%i] (%u)\n", stacks->b->values[i], stacks->b->ranks[i]);
	}
}

void	compute_stats(t_stacks *stacks, t_args *parsed_args, t_stats *stats)
{
	reset_op_stats(stats);
	stats->nb_ints = parsed_args->nb_ints;
	stats->disorder_perc = compute_disorder_perc(stacks->a);
	stats->is_adaptive = (parsed_args->strategy == ADAPTIVE);
	if (stats->is_adaptive)
		stats->actual_strategy = get_strategy(stats->disorder_perc,
				stats->nb_ints);
	else
		stats->actual_strategy = parsed_args->strategy;
	stacks->stats = stats;
}
