/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 14:55:14 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/07 10:45:08 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	nbr;
	int	i;

	i = 1;
	nbr = nb;
	if (nbr > 0)
	{
		while (i != nb)
		{
			nbr *= nb - i;
			i++;
		}
		return (nbr);
	}
	else if (nbr == 0)
		return (1);
	else
		return (0);
}
/*
#include <stdio.h>
int	main(void)
{
	printf("%d\n", ft_iterative_factorial(5));
	ft_iterative_factorial(2);
	ft_iterative_factorial(3);
	ft_iterative_factorial(10);
	ft_iterative_factorial(5);
	return (0);
}*/
