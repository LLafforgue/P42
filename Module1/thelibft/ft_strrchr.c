/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 13:49:47 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 13:49:49 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char	*ft_strrchr(const char *s, int c)
{
	const char	*deb;

	deb = s;
	while (*s)
		s++;
	while (*s != c % 256 && s > deb)
	{
		s--;
		if (s == deb && *s == c % 256)
			return ((char *)s);
	}
	if (s == deb && *deb != c)
		return ((void *)0);
	else
		return ((char *)s);
}
/*
int main(void)
{
    const char *str = "";
    char *test = ft_strrchr(str, 0);
	if (test)
    	printf("%s\n", test);
	else
		printf("%p\n", test);
}

*/