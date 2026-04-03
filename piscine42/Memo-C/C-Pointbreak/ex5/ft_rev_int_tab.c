/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 16:46:04 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 13:27:40 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
#include <stdio.h>
#include <stdlib.h>
*/
void	ft_rev_int_tab(int *tab, int size)
{
	int	relais;
	int	i;

	i = 0;
	while (i < size / 2)
	{
		relais = tab[i];
		tab[i] = tab[size - i - 1];
		tab[size - i - 1] = relais;
		i++;
	}
}
/*
int  main(void)
{
 int tab[3] = {0,1,2};
 ft_rev_int_tab(tab, 3);
 printf("tab[2] est %d\n", tab[2]);
 printf("tab[1] est %d\n", tab[1]);
 printf("tab[0] est %d\n", tab[0]);
 return (0);
}
*/
