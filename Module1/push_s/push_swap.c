/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 15:10:07 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 18:10:12 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	sort_with_strategy(t_stacks *stacks, t_e_strat strategy)
{
	if (strategy == COMPLEX)
		radix_sort(stacks);
	else if (strategy == MEDIUM)
		bucket_sort(stacks);
	else
		min_extract_sort(stacks);
}

int	main(int argc, char **argv)
{
	t_stacks	stacks;
	t_stats		stats;
	t_args		parsed_args;

	parsed_args = parse_args(argc - 1, argv + 1);
	if (!init_stacks(&stacks, parsed_args.nb_ints))
		clean_exit_with_error(MALLOC_ERROR, &stacks);
	fill_stack_a(argc - 1, argv + 1, &stacks);
	compute_stats(&stacks, &parsed_args, &stats);
	sort_with_strategy(&stacks, stats.actual_strategy);
	if (parsed_args.bench_mode)
	{
		display(&stacks);
		display_bench(&stats);
	}
	free_stacks(&stacks);
}
