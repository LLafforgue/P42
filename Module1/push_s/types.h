/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   types.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/22 14:43:58 by osasburg          #+#    #+#             */
/*   Updated: 2025/12/01 14:11:43 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef TYPES_H
# define TYPES_H

# include <stdbool.h>
# include <stdlib.h>

typedef enum strategy
{
	NO_STRATEGY,
	SIMPLE,
	MEDIUM,
	COMPLEX,
	ADAPTIVE
}	t_e_strat;

typedef enum ops
{
	PA,
	PB,
	RA,
	RB,
	RR,
	RRA,
	RRB,
	RRR,
	SA,
	SB,
	SS,
	OPS_END
}	t_e_ops;

typedef struct s_args
{
	size_t		nb_ints;
	t_e_strat	strategy;
	bool		bench_mode;
}	t_args;

typedef struct s_stats
{
	float			disorder_perc;
	bool			is_adaptive;
	t_e_strat		actual_strategy;
	unsigned int	op_calls[OPS_END];
	unsigned int	total_ops;
	size_t			nb_ints;
}	t_stats;

typedef struct s_stack
{
	int				*values;
	unsigned int	*ranks;
	size_t			len;
	size_t			max_size;
}	t_stack;

typedef struct s_stacks
{
	size_t	max_size;
	t_stack	*a;
	t_stack	*b;
	t_stats	*stats;
}	t_stacks;

typedef unsigned long	t_pos;

#endif