/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 16:27:45 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/06 12:14:33 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

//Fonction qui affiche une string de deux caracteres
void	ft_affiche_duo(char buff[2])
{
	int	i;

	i = 2;
	while (i > 0)
	{
		write(1, &buff[--i], 1);
	}
}

//Fonction qui change un entier en string affichee
void	ft_int_to_print_string(int c)
{
	char	uplet[2];
	int		i;

	uplet[0] = '0';
	uplet[1] = '0';
	i = 0;
	while (c > 0)
	{
		uplet[i++] = '0' + (c % 10);
		c /= 10;
	}
	ft_affiche_duo(uplet);
}

//Fonction pricipale
void	ft_print_comb2(void)
{
	int		m;
	int		n;

	m = 0;
	n = 2;
	write(1, "00 01", 5);
	while (m <= 98)
	{
		if (m < n)
		{
			while (n <= 99)
			{
				write(1, ", ", 2);
				ft_int_to_print_string(m);
				write(1, " ", 1);
				ft_int_to_print_string(n);
				n ++;
			}
			m ++;
			n = m + 1;
		}
	}
}

/*int main()
{
	ft_print_comb2();
	return (0);
}*/
