/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 14:45:45 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/03 15:00:45 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

char	*ft_strdup(const char *str)
{
	char		*dup;
	const char	*temp;

	temp = str;
	while (*str)
		str++;
	dup = malloc(sizeof(char) * (str - temp + 1));
	if (!dup)
		return (NULL);
	str = temp;
	temp = dup;
	while (*str)
	{
		*dup++ = *str;
		str++;
	}
	*dup = '\0';
	return ((char *)temp);
}
