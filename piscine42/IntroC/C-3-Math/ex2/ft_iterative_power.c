/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 16:59:26 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/07 09:33:47 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_spe(int power)
{
	if (power < 0)
		return (0);
	return (2);
}

int	ft_iterative_power(int nb, int power)
{
	int	nbr;

	nbr = 1;
	if (ft_spe(power) != 2)
		return (ft_spe(power));
	else
	{
		while (power >= 1)
		{
			nbr *= nb;
			power--;
		}
		return (nbr);
	}
}

/*int  main(void)
{
	int poweeer;
	poweeer = ft_iterative_power(2, 4);
	printf("La valeur retournee est :%d\n", poweeer);
	poweeer = ft_iterative_power(2, 0);
	printf("La valeur retournee est :%d\n", poweeer);
	return (0);
}*/
