/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 16:17:10 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/22 18:36:01 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	i;

	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	*range = malloc((max - min) * sizeof(int));
	if (*range == NULL)
		return (-1);
	i = 0;
	while (i < max - min)
	{
		(*range)[i] = min + i;
		i++;
	}
	return (i);
}
/*
#include <stdio.h>

int  main(void)
{
	int min = -1;
	int max = -1;
	int i = 0;
	int	*range;

	int res = ft_ultimate_range(&range, min, max);
	printf("La taille de range : %d\n", res);
	while(i != max - min)
	{
		printf("%d ", *(range + i));
		i ++;
	}
	free(range);
	return (0);
}
*/
