/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:43:09 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 11:04:38 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	len_s;
	size_t	i;

	i = 0;
	if (dst == NULL || src == NULL || size == 0)
		return (ft_strlen(src));
	len_s = ft_strlen(src);
	while (*src && i < size - 1)
		dst[i++] = *src++;
	dst[i] = '\0';
	return (len_s);
}
/*
#include <stdio.h>
int main(void)
{
	size_t len;
	char src[] = "coucou";
	char dest[10]; ft_memset(dest, 'A', 10);
	printf("L'original est : %s\n", src);
	len = ft_strlcpy(dest, src, 1);
	printf("La taille de retour est %ld\nCopy : %s\n", len, dest);
	printf("%c\n", dest[2]);
}
*/