/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 11:09:19 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 11:09:37 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	len_s;
	size_t	len_d;
	size_t	i;

	len_s = ft_strlen(src);
	len_d = ft_strlen(dst);
	i = 0;
	if (len_d >= size)
		return (len_s + size);
	while (dst[i])
		i++;
	while (i < size - 1 && *src)
		dst[i++] = *src++;
	dst[i] = '\0';
	return (len_d + len_s);
}
/*
int main(void)
{
	
	char dest[30]; 
	ft_memset(dest, 0, 30);
	char * src = (char *)"AAAAAAAAA";
	ft_memset(dest, 'B', 4);
	int test = ft_strlcat(dest, src, 6);
	printf("%s\n", dest);
	printf("%d\n", test);
}
*/