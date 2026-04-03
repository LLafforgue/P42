/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_str.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 15:10:19 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/17 17:07:55 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_put_str(char *s)
{
	char	*temp;

	if (s)
	{
		temp = s;
		while (*s)
			s++;
		return (write(1, temp, s - temp));
	}
	return (write(1, "(null)", 6));
}
