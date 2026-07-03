/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 14:38:26 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/05 14:38:30 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_empty(void)
{
	char	*copy;

	copy = malloc(sizeof(char));
	if (!copy)
		return (NULL);
	*copy = '\0';
	return (copy);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*copy;
	char	*temp;
	size_t	i;

	while (start-- && *s)
		s++;
	i = ft_strlen(s);
	if (*s && len != 0)
	{
		if (i < len)
			len = i;
		copy = malloc((len + 1) * sizeof(char));
		if (!copy)
			return (NULL);
		temp = copy;
		while (len && *s)
		{
			*copy++ = *s++;
			len--;
		}
		*copy = '\0';
		return (temp);
	}
	return ((char *)ft_empty());
}
/*
#include <stdio.h>
int main(void)
{
	char * s = ft_substr("tripouille", 0, 42000);

	printf("%s\n", s);
	free(s);
}
*/