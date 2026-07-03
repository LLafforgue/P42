/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/02 13:42:31 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/03 12:08:19 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void	ft_print_comb(void)
{
	char	n;
	char	m;
	char	i;

	n = '0';
	while (n <= '7')
	{
		m = n + 1;
		while (m <= '8')
		{
			i = m + 1;
			while (i <= '9')
			{
				write(1, &n, 1);
				write(1, &m, 1);
				write(1, &i, 1);
				if (!(n == '7' && i == '9'))
					write(1, ", ", 2);
				i ++;
			}
			m ++;
		}
		n ++;
	}
	return ;
}

/*int main ()
{
		ft_print_comb();
		return (0);
}*/
