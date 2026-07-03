/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 17:55:32 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/22 14:43:10 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*range;
	int	i;

	if (!(max - min > 0))
		return (NULL);
	range = malloc((max - min) * sizeof(int));
	i = 0;
	while (i < max - min)
	{
		range[i] = min + i;
		i++;
	}
	return (range);
}
/*
#include <stdio.h>

int  main(void)
{
	int min = -1;
	int max = 4;
	int i = 0;
	printf("Pour min %d et max %d\n", min, max);
	while(i < max - min)
	{
		printf("%d ", *(ft_range(min, max) + i));
		i ++;
	}
	return (0);
}
*/
