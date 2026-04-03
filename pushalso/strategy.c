/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strategy.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 10:44:58 by llafforg          #+#    #+#             */
/*   Updated: 2026/02/24 14:23:03 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	ft_check_disorder(t_data *data)
{
	if (data->disorder >= 0 && data->disorder < 20)
		simple_algo(data);
	else if (data->disorder >= 20 && data->disorder < 50)
		medium_algo(data);
	else
		algo_complex(data);
}

void	set_strategy(t_args *args, t_data *data)
{
	if (args->flag_simple)
		simple_algo(data);
	else if (args->flag_medium)
		medium_algo(data);
	else if (args->flag_complex)
		algo_complex(data);
	else
		ft_check_disorder(data);
}
