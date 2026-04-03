/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 13:49:35 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/06 13:49:37 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	size_t	cnt;

	cnt = 0;
	while (lst != NULL)
	{
		cnt++;
		lst = lst->next;
	}
	return (cnt);
}
/*
#include <stdio.h>
int main (void)
{
    t_list *head = (void *)0;

    t_list m3 = {NULL, NULL};
    t_list m2 = {NULL, &m3};
    t_list m1 = {NULL, &m2};
    head = &m1;
    size_t test = ft_lstsize(head);
    printf("il y a %ld maillons dans le chaine.\n", test);
    return (0);
}
*/
