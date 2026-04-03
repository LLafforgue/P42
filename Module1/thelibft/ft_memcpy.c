/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 17:30:18 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 09:56:47 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t				i;
	unsigned char		*temp;
	const unsigned char	*srctp;

	i = 0;
	temp = dest;
	srctp = src;
	if (dest == NULL)
		return (NULL);
	while (i < n)
	{
		temp[i] = srctp[i];
		i++;
	}
	return (dest);
}
/*
#include "libft.h"
#include <stdio.h>
int main(void)
{
	
	char dest[100];
	ft_memset(dest, 'A', 10);
	ft_memcpy(dest, "coucou", 0);
	char *rtn = (char *)ft_memcpy(dest, NULL, 0);
	printf("%s\n", rtn);
	printf("%c\n", dest[0]);
	return (0);
}
*/