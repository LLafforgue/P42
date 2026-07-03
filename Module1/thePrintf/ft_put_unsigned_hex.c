/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_unsigned_hex.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:10:10 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/17 15:13:31 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static int	ft_write_nbr_low(unsigned int n)
{
	char	buff[13];
	int		i;
	int		len;

	i = 0;
	len = 0;
	while (n > 0)
	{
		buff[i++] = "0123456789abcdef"[n % 16];
		n /= 16;
		len++;
	}
	while (i > 0)
		write(1, &buff[--i], 1);
	return (len);
}

static int	ft_write_nbr_up(unsigned int n)
{
	char	buff[13];
	int		i;
	int		len;

	i = 0;
	len = 0;
	while (n > 0)
	{
		buff[i++] = "0123456789ABCDEF"[n % 16];
		n /= 16;
		len++;
	}
	while (i > 0)
		write(1, &buff[--i], 1);
	return (len);
}

int	ft_put_unsigned_hex(unsigned int n, int s)
{
	int	len;

	len = 0;
	if (n == 0)
		return (write(1, "0", 1));
	if (s == 0)
		len += ft_write_nbr_low(n);
	if (s == 1)
		len += ft_write_nbr_up(n);
	return (len);
}
