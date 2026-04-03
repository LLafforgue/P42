/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_unsigned_nbr.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:10:10 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/17 15:10:54 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static int	ft_write_nbr(unsigned int n)
{
	char	buff[13];
	int		i;
	int		len;

	i = 0;
	len = 0;
	while (n > 0)
	{
		buff[i++] = n % 10 + '0';
		n /= 10;
		len++;
	}
	while (i > 0)
		write(1, &buff[--i], 1);
	return (len);
}

int	ft_put_unsigned_nbr(unsigned int n)
{
	int		len;

	len = 0;
	if (n == 0)
		return (write(1, "0", 1));
	len += ft_write_nbr(n);
	return (len);
}
/*
int main(void)
{
	ft_putnbr_fd(9514, 1);
}
*/
