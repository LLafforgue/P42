
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 15:52:09 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/06 16:51:26 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	int	nbr;
	nbr = 1;
	if (nb > 0)
	{
		nbr =  nb * ft_iterative_factorial(nb - 1);
		printf("nbr est %d\n", nbr);
		return nbr;
	}
	else if (nb == 0)
		{
		printf("nbr est %d\n", nbr);
		return (1);
		}
	else
		return (0);
}

int	main(void)
{
	ft_iterative_factorial(5);
	return (0);
}