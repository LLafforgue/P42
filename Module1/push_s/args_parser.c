/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   args_parser.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:44:20 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 14:55:48 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "args_parser.h"
#include "error_mgmt.h"
#include "libft.h"

static void	set_strategy(t_args *parsed_args, t_e_strat strat)
{
	if (parsed_args->strategy != NO_STRATEGY && parsed_args->strategy != strat)
		clean_exit_with_error(INCONSISTENT_ARGS_ERROR, NULL);
	parsed_args->strategy = strat;
}

static void	parse_named_arg(char *named_arg, t_args *args)
{
	if (ft_strncmp(named_arg, "bench", ARG_LEN_MAX) == 0)
		args->bench_mode = true;
	else if (ft_strncmp(named_arg, "simple", ARG_LEN_MAX) == 0)
		set_strategy(args, SIMPLE);
	else if (ft_strncmp(named_arg, "medium", ARG_LEN_MAX) == 0)
		set_strategy(args, MEDIUM);
	else if (ft_strncmp(named_arg, "complex", ARG_LEN_MAX) == 0)
		set_strategy(args, COMPLEX);
	else if (ft_strncmp(named_arg, "adaptive", ARG_LEN_MAX) == 0)
		set_strategy(args, ADAPTIVE);
	else
		clean_exit_with_error(INVALID_ARG_ERROR, NULL);
}

static void	check_num_arg(char *num, t_args *args)
{
	int	res;

	if (!ft_atoi(num, &res))
		clean_exit_with_error(INVALID_NUM_ERROR, NULL);
	args->nb_ints++;
}

t_args	parse_args(int argc, char **argv)
{
	t_args	args;
	int		i;

	args.strategy = NO_STRATEGY;
	args.bench_mode = false;
	args.nb_ints = 0;
	i = 0;
	while (i < argc)
	{
		if (argv[i][0] == '-' && argv[i][1] == '-')
			parse_named_arg(argv[i] + 2, &args);
		else
			check_num_arg(argv[i], &args);
		i++;
	}
	if (args.strategy == NO_STRATEGY)
		args.strategy = ADAPTIVE;
	if (args.nb_ints == 0)
		exit(0);
	return (args);
}
