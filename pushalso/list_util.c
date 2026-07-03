/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_util.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 13:57:25 by smlamali          #+#    #+#             */
/*   Updated: 2026/01/08 15:43:24 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*ft_lstnew(int nbr)
{
	t_stack	*new;

	new = malloc(sizeof(t_stack));
	if (!new)
		return (NULL);
	new->nbr = nbr;
	new->index = 0;
	new->next = NULL;
	return (new);
}

void	ft_lstadd_back(t_stack **stack, t_stack *new)
{
	t_stack	*tmp;

	if (!*stack)
		*stack = new;
	else
	{
		tmp = *stack;
		while (tmp->next != NULL)
			tmp = tmp->next;
		tmp->next = new;
	}
}

void	ft_lstadd_front(t_stack **lst, t_stack *new)
{
	new->next = *lst;
	*lst = new;
}

int	ft_lstsize(t_stack *stack)
{
	int	c;

	c = 0;
	if (!stack)
		return (c);
	while (stack)
	{
		c++;
		stack = stack->next;
	}
	return (c);
}

void	ft_lstprint(t_stack *stack)
{
	char	*n_str;

	if (!stack)
		return ;
	while (stack)
	{
		n_str = ft_itoa(stack->nbr);
		ft_putstr("[", 1);
		ft_putstr(n_str, 1);
		ft_putstr("]->", 1);
		stack = stack->next;
		free(n_str);
	}
	ft_putstr("NULL\n", 1);
}

// void	ft_lstprint_index(t_stack *stack)
// {
// 	char	*n_str;

// 	if (!stack)
// 		return ;
// 	while (stack)
// 	{
// 		n_str = ft_itoa(stack->index);
// 		ft_putstr("[", 1);
// 		ft_putstr(n_str, 1);
// 		ft_putstr("]->", 1);
// 		stack = stack->next;
// 		free(n_str);
// 	}
// 	ft_putstr("NULL\n", 1);
// }