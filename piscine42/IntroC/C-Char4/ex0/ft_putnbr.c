/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 11:11:47 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/02 16:25:49 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(int nb)
{
	int		i;
	char	buff[11];

	i = 0;
	if (nb == 0)
		write(1, "0", 1);
	if (nb == -2147483648)
		write(1, "-2147483648", 11);
	if (nb < 0 && nb > -2147483648)
	{
		write(1, "-", 1);
		nb = -nb;
	}
	while (nb > 0)
	{
		buff[i++] = '0' + (nb % 10);
		nb /= 10;
	}
	while (i > 0)
	{
		write(1, &buff[--i], 1);
	}
}

/*int main()
{
	ft_putnbr(42);
	ft_putnbr(-2);
	ft_putnbr(-2147483648);
        ft_putnbr(0);
	return(0);
}*/
