/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_mgmt.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 16:06:25 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/28 18:23:37 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"
#include "error_mgmt.h"
#include "libft.h"
#include "stack_mgmt.h"

bool	init_stacks(t_stacks *stacks, size_t size)
{
	stacks->max_size = size;
	stacks->a = malloc(sizeof(t_stack));
	stacks->b = malloc(sizeof(t_stack));
	if (stacks->a == NULL || stacks->b == NULL)
		return (false);
	stacks->a->len = 0;
	stacks->a->max_size = size;
	stacks->a->values = malloc(size * sizeof(int));
	stacks->a->ranks = malloc(size * sizeof(unsigned int));
	stacks->b->len = 0;
	stacks->b->max_size = size;
	stacks->b->values = malloc(size * sizeof(int));
	stacks->b->ranks = malloc(size * sizeof(unsigned int));
	return (stacks->a->values && stacks->a->ranks && stacks->b->values
		&& stacks->b->ranks);
}

unsigned int	find_rank(int *sorted, int value)
{
	unsigned int	i;

	i = 0;
	while (true)
	{
		if (sorted[i] == value)
			return (i);
		i++;
	}
}

int	*rank_stack(t_stack *stack)
{
	size_t	i;
	int		*sorted;

	sorted = malloc(stack->len * sizeof(int));
	if (sorted)
	{
		ft_memcpy(sorted, stack->values, stack->len * sizeof(int));
		quick_sort(sorted, stack->len);
		i = 0;
		while (i < stack->len)
		{
			stack->ranks[i] = find_rank(sorted, stack->values[i]);
			i++;
		}
	}
	return (sorted);
}

bool	has_duplicates(int *sorted_nums, size_t len)
{
	while (--len > 0)
		if (sorted_nums[len - 1] == sorted_nums[len])
			return (true);
	return (false);
}

void	fill_stack_a(int count, char **args, t_stacks *stacks)
{
	int		i;
	int		*sorted_nums;
	bool	has_dups;

	i = -1;
	while (++i < count)
	{
		if (args[i][0] && args[i][1] != '-')
			ft_atoi(args[i], stacks->a->values + stacks->a->len++);
	}
	sorted_nums = rank_stack(stacks->a);
	if (!sorted_nums)
		clean_exit_with_error(MALLOC_ERROR, stacks);
	has_dups = has_duplicates(sorted_nums, stacks->a->len);
	free(sorted_nums);
	if (has_dups)
		clean_exit_with_error(DUPLICATE_NUM_ERROR, stacks);
}
