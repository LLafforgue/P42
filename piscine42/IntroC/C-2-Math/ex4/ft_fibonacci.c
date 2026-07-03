/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fibonacci.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/06 17:35:28 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/07 09:37:35 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_fibonacci(int index)
{
	int	x;

	x = 1;
	if (index < 0)
		return (-1);
	if (index == 0)
		return (0);
	if (index > 1)
		return (ft_fibonacci(index - 1) + ft_fibonacci(index - 2));
	return (x);
}
/*
int  main(void)
{
	int fifi;
	fifi = ft_fibonacci(6);
	printf("La valeur retournee est :%d\n", fifi);
 return (0);
}
*/
