/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush01.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/04 12:05:08 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/04 14:09:49 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

void	ft_display_at(int x, int y, int col, int li)
{
	if ((x == 0 && y == 0) || (x == col - 1 && y == li - 1))
	{
		ft_putchar('/');
		return ;
	}
	else if ((x == 0 && y == li - 1) || (x == col - 1 && y == 0))
	{
		ft_putchar('\\');
	}
	else if ((x != 0 && y !=0 && x != col - 1 && y != li - 1))
	{
		ft_putchar(' ');
	}
	else
		ft_putchar('*');
}

int	ft_error(int col, int li)
{
	if (col <= 0 || li <= 0 || col > 317 || li > 317)
	{
		write(1, "ERROR!\n", 7);
		return (1);
	}
	return (0);
}

void	rush(int col, int li)
{
	int	x;
	int	y;

	if (ft_error(col, li) == 1)
		return ;
	x = 0;
	y = 0;
	while (y < li)
	{
		while (x < col)
		{
			ft_display_at(x, y, col, li);
			x++;
		}
		x = 0;
		ft_putchar('\n');
		y++;
	}
}
