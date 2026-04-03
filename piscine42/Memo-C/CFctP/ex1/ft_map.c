/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:02:11 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 13:44:16 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>

int	*ft_map(int *tab, int length, int (*f)(int))
{
	int	*rep;
	int	i;

	rep = (int *) malloc(length * sizeof(int));
	if (rep == NULL)
		return (0);
	i = -1;
	while (++i < length)
		*(rep + i) = f(*(tab + i));
	return (rep);
}
/*
int ft_test(int nbr)
{
	return (nbr + 10);
}

int main(void)
{
	int	tab[3] = {1, 12, 3};
	int *rep;
	int	i;

	i = -1;
	rep = ft_map(tab, 3, &ft_test);
	while (++i < 3)
		printf("%d ", rep[i]);
	return (0);
}
*/
