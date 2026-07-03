/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_foreach.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:01:36 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 13:43:58 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_foreach(int *tab, int length, void (*f)(int))
{
	int	i;

	i = 0;
	while (i < length)
	{
		f(*(tab + i));
		i ++;
	}
}
/*
void	ft_test(int nbr)
{
	char	nb[11];
	int		i;

	i = 0;
	if (nbr == 0)
	{
		write(1, "0", 1);
		return ;
	}
	if (nbr < 0)
	{
		write(1, "NON", 3);
		return ;
	}
	while (nbr > 0)
	{
		nb[i++] = '0' + nbr % 10;
		nbr /= 10;
	}
	while (i != 0)
		write(1, &nb[--i], 1);
}

int main(void)
{
	int buff[5] = {1, 25, -5, 0, 24};
	ft_foreach(buff, 5, &ft_test);
}
*/
