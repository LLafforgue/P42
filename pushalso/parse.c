/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 13:55:06 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 14:51:36 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	check_strategy(t_args *args, t_errors *errors)
{
	int	count;

	count = 0;
	if (args->flag_simple)
		count++;
	if (args->flag_medium)
		count++;
	if (args->flag_complex)
		count++;
	if (args->flag_adaptive)
		count++;
	if (count > 1)
	{
		errors->error_strategy = 1;
		ft_display_errors(*errors);
		return (0);
	}
	return (1);
}

static int	is_a_flag(char *str, t_args *args, t_errors *errors)
{
	if (ft_strncmp(str, "--bench", 8) == 0)
	{
		args->flag_bench = 1;
		return (1);
	}
	else if (ft_strncmp(str, "--simple", 9) == 0
		|| ft_strncmp(str, "--medium", 9) == 0
		|| ft_strncmp(str, "--complex", 11) == 0
		|| ft_strncmp(str, "--adaptive", 11) == 0)
	{
		if (ft_strncmp(str, "--simple", 9) == 0)
			args->flag_simple = 1;
		else if (ft_strncmp(str, "--medium", 9) == 0)
			args->flag_medium = 1;
		else if (ft_strncmp(str, "--complex", 11) == 0)
			args->flag_complex = 1;
		else if (ft_strncmp(str, "--adaptive", 11) == 0)
			args->flag_adaptive = 1;
		return (check_strategy(args, errors));
	}
	errors->error_args = 1;
	return (0);
}

//check if argument is a rational integer
int	is_valid(char *str, t_args *args, t_errors *errors)
{
	int	i;
	int	valid;

	i = 0;
	valid = 1;
	if (!str)
		return (0);
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			valid = 0;
		i++;
	}
	if (!valid)
		if (is_a_flag(str, args, errors) != 1)
			return (0);
	return (1);
}

static int	has_space(char *arg)
{
	while (*arg)
	{
		if (*arg == ' ')
			return (1);
		arg++;
	}
	return (0);
}

int	ft_check_parse(char **arg, t_stack **a, t_args *args, t_errors *errors)
{
	int	i;

	i = 0;
	if (!arg)
		return (0);
	init_flags(args, errors);
	while (arg[i])
	{
		if ((!*arg[i] || !is_valid(arg[i], args, errors))
			&& !has_space(arg[i]))
			return (ft_display_errors(*errors), 0);
		i++;
		errors->error_args = 0;
	}
	while (*arg)
	{
		if (!has_space(*arg))
			ft_put_nbr_stack(*arg++, a, errors);
		else if (parse_splited(*arg++, a, args, errors) == 0)
			return (0);
	}
	if (ft_check_stack(a, errors))
		return (0);
	return (1);
}
