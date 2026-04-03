/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 16:08:59 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/27 14:28:34 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	ft_print_operations(int fd, t_data *data)
{
	write(fd, "[bench] sa:\t", 12);
	ft_putnbr_fd(fd, data->sa);
	write(fd, "\tsb:\t", 6);
	ft_putnbr_fd(fd, data->sb);
	write(fd, "\tss:\t", 6);
	ft_putnbr_fd(fd, data->ss);
	write(fd, "\tpa:\t", 6);
	ft_putnbr_fd(fd, data->pa);
	write(fd, "\tpb:\t", 6);
	ft_putnbr_fd(fd, data->pb);
	write(fd, "\n[bench] ra:\t", 13);
	ft_putnbr_fd(fd, data->ra);
	write(fd, "\trb:\t", 6);
	ft_putnbr_fd(fd, data->rb);
	write(fd, "\trr:\t", 6);
	ft_putnbr_fd(fd, data->rr);
	write(fd, "\trra:\t", 7);
	ft_putnbr_fd(fd, data->rra);
	write(fd, "\trrb:\t", 7);
	ft_putnbr_fd(fd, data->rrb);
	write(fd, "\trrr:\t", 6);
	ft_putnbr_fd(fd, data->rrr);
}

static void	ft_print_opti(int fd, t_data *data)
{
	int	total;

	total = data->sa + data->sb + data->ss;
	total += data->pa + data->pb;
	total += data->ra + data->rb + data->rr;
	total += data->rra + data->rrb + data->rrr;
	write(fd, "[bench] total_ops:	", 20);
	ft_putnbr_fd(fd, total);
	write(fd, "\n", 1);
}

void	print_bench(int fd, t_data *data, t_args args)
{
	write(fd, "[bench] disorder:	", 18);
	ft_put_disorder(fd, data->disorder);
	write(fd, "[bench] strategy:	", 19);
	if (args.flag_simple)
		write(fd, "Simple / O(n²)\n", 17);
	else if (args.flag_medium)
		write(fd, "Medium / O(n√n)\n", 18);
	else if (args.flag_complex)
		write(fd, "Complex / O(nlogn)\n", 19);
	else
	{
		write(fd, "Adaptive / ", 11);
		if (data->disorder >= 0 && data->disorder < 20)
			write(fd, "O(n)\n", 6);
		if (data->disorder >= 20 && data->disorder < 50)
			write(fd, "O(n√n)\n", 9);
		if (data->disorder >= 50)
			write(fd, "O(nlogn)\n", 9);
	}
	ft_print_opti(fd, data);
	ft_print_operations(fd, data);
	write(fd, "\n", 1);
}
