/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 17:13:21 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/07 15:30:10 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_spe(int power)
{
	if (power == 0)
		return (1);
	if (power < 0)
		return (0);
	return (2);
}

int	ft_recursive_power(int nb, int power)
{
	if (ft_spe(power) != 2)
		return (ft_spe(power));
	else
	{
		if (power >= 0)
			return (nb * ft_recursive_power(nb, power - 1));
		else
			return (nb);
	}
}
/*
int  main(void)
{
	int poweeer;
	poweeer = ft_recursive_power(2, 10);
	printf("La valeur retournee est :%d\n", poweeer);
	return (0);
}
*/
