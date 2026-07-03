/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_util_bis.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 15:43:13 by llafforg          #+#    #+#             */
/*   Updated: 2026/01/08 15:43:48 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_lstclear(t_stack **stack)
{
	t_stack	*temp;
	t_stack	*next_node;

	if (!stack || !*stack)
		return ;
	temp = *stack;
	while (temp)
	{
		next_node = temp->next;
		free(temp);
		temp = next_node;
	}
	*stack = NULL;
}
