/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 14:40:50 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/06 14:40:53 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	else
		while (lst->next != NULL)
			lst = lst->next;
	return (lst);
}
/*
#include <stdio.h>
int main (void)
{
    t_list *head = (void *)0;
    t_list m3 = {"last", NULL};
    t_list m2 = {NULL, &m3};
    t_list m1 = {NULL, &m2};
    head = &m1;
    t_list *test = ft_lstlast(head);
	char	*content = (char *)(test->content);
    printf("on a bien le %s maillon.\n", content);
    return (0);
}
*/
