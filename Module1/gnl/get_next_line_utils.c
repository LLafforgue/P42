/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 11:30:07 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/20 15:00:49 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	ft_strlen(char *s)
{
	char	*temp;

	temp = s;
	while (*s)
		s++;
	return (s - temp);
}

void	*ft_calloc_empty(size_t size)
{
	char	*alloc;

	alloc = malloc(size * sizeof(char));
	if (!alloc)
		return (NULL);
	while (size)
		alloc[--size] = '\0';
	return (alloc);
}

int	ft_chek_line(char *str)
{
	while (*str)
	{
		if (*str++ == SEPARATOR)
			return (1);
	}
	return (0);
}

void	*ft_error(char *str)
{
	free(str);
	return (NULL);
}
