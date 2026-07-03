/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 16:32:06 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 13:33:15 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	relais;

	relais = *a;
	*a = relais / *b;
	*b = relais % *b;
}
/*
int  main(void)
{
 int a = 19;
 int b = 10;
 ft_ultimate_div_mod(&a, &b);
 printf("a est %d ; b est %d\n", a, b);
 return (0);
}
*/
