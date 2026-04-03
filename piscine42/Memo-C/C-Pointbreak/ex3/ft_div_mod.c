/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/07 16:24:21 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/07 16:31:10 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}

/*
int  main(void)
{
 int x;
 int rest;
 ft_div_mod(19, 10, &x, &rest);
 printf("quotient : %d, reste : %d\n", x, rest);
 return (0);
}
*/
