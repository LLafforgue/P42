/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 13:56:36 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 17:21:59 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_display_errors(t_errors errors)
{
	char	*number;

	if (errors.error_args)
		ft_putstr("Error: Invalid argument(s) provided.\n", 2);
	if (errors.error_strategy)
		ft_putstr("Error: Multiple strategy flags provided.\n", 2);
	if (errors.error_no_stack)
		ft_putstr("Error: Empty stacks.\n", 2);
	if (errors.error_duplicate)
	{
		ft_putstr("Error: There are duplicate numbers in the stack (ex ", 2);
		number = ft_itoa(errors.error_duplicate);
		ft_putstr(number, 2);
		write(2, ")\n", 2);
		free(number);
	}
	if (errors.error_max)
		ft_putstr("Error: Max or Min value found!\n", 2);
}

static void	ft_free_alloc(t_data *data)
{
	ft_lstclear(data->a);
	ft_lstclear(data->b);
	free(data);
}

void	init_datas(t_data *data, t_stack **a, t_stack **b)
{
	ft_set_index(*a);
	data->a = a;
	data->b = b;
	data->len_a = ft_lstsize(*a);
	data->len_b = 0;
	data->sa = 0;
	data->sb = 0;
	data->ra = 0;
	data->rb = 0;
	data->rr = 0;
	data->ss = 0;
	data->pa = 0;
	data->pb = 0;
	data->rra = 0;
	data->rrb = 0;
	data->rrr = 0;
	ft_disorder(data);
}

int	main(int argc, char **argv)
{
	t_stack		*a;
	t_stack		*b;
	t_args		args;
	t_errors	errors;
	t_data		*data;

	a = NULL;
	b = NULL;
	if (argc == 1)
		return (0);
	argv++;
	if (!ft_check_parse(argv, &a, &args, &errors))
		return (1);
	data = malloc(sizeof(t_data));
	if (!data)
		return (0);
	init_datas(data, &a, &b);
	set_strategy(&args, data);
	if (args.flag_bench)
		print_bench(2, data, args);
	ft_free_alloc(data);
}
