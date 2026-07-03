/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 16:49:59 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/06 16:50:02 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putendl_fd(char *s, int fd)
{
	char	*temp;

	if (s)
	{
		temp = s;
		while (*s)
			s++;
		write(fd, temp, s - temp);
	}
	write(fd, "\n", 1);
}
