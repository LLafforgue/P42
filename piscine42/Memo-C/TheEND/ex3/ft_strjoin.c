/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 16:57:03 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/23 14:56:43 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	strs_len(char **strs, int size, int j)
{
	int	i;

	i = 0;
	if (j == size)
		return (i);
	while (*(*strs + i) != '\0')
		i++;
	return (i + strs_len((strs + 1), size, j + 1));
}

void	ft_copy(char *join, int size, char **strs, char *sep)
{
	int		i;
	int		j;

	i = 0;
	j = 0;
	while (i < size)
	{
		while ((strs[i][j] != '\0'))
			*join++ = strs[i][j++];
		j = 0;
		if (i != size - 1)
		{
			while (sep[j] != '\0')
				*join++ = sep[j++];
			j = 0;
		}
		else
			*join = '\0';
		i++;
	}
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*join;
	int		len;
	char	*n;

	if (!sep || !strs)
		return (NULL);
	if (size == 0)
	{
		join = malloc(1);
		join[0] = '\0';
		return (join);
	}
	len = strs_len(strs, size, 0) + size * strs_len(&sep, 1, 0);
	join = malloc(len * sizeof(char));
	if (join == NULL)
		return (NULL);
	n = join;
	ft_copy(join, size, strs, sep);
	return (n);
}
/*
#include <stdio.h>

int  main(void)
{
	char *strs[3];
	strs[0] = "un";
	strs[1] = "deux";
	strs[2] = "trois";
	char *sep = " - ";
	char *join;

	join = ft_strjoin(3, strs, sep);
	if(join)
		printf("%s\n", join);
 return (0);
}

*/
