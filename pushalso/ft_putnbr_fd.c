/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 16:53:36 by llafforg          #+#    #+#             */
/*   Updated: 2026/01/16 12:04:40 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#define INT_MIN -2147483648

void	ft_putnbr_fd(int fd, int n)
{
	int		i;
	char	buff[13];

	if (n == INT_MIN)
	{
		write(fd, "-2147483648", 11);
		return ;
	}
	if (n == 0)
		write(fd, "0", 1);
	if (n < 0)
	{
		n *= -1;
		write(fd, "-", 1);
	}
	i = 0;
	while (n > 0)
	{
		buff[i++] = n % 10 + '0';
		n /= 10;
	}
	while (i > 0)
		write(fd, &buff[--i], 1);
}
