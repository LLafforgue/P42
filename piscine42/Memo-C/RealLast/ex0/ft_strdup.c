/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 17:53:54 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/22 16:07:24 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	str_len(char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*i;
	int		length;
	char	*copy;

	if (src == NULL)
		return (NULL);
	length = str_len(src);
	copy = malloc((length + 1) * sizeof(char));
	if (copy == NULL)
		return (NULL);
	i = copy;
	while (*src != '\0')
		*copy++ = *src++;
	return (i);
}
/*
#include <stdio.h>

int  main(void)
{
	char *original;
	char *copy;

	original = NULL;
	copy = ft_strdup(original);
	printf("l'original :%s\n", original);
	printf("la copie :%s\n", copy);

 return (0);
}
*/
