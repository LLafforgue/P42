/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush00.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <osasburg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/04 11:23:43 by osasburg          #+#    #+#             */
/*   Updated: 2025/10/04 12:56:44 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

int	check_valid(int x, int y)
{
	int	min;
	int	max;
	int	is_valid;

	min = 0;
	max = 317;
	is_valid = (x >= min && x <= max && y >= min && y <= max);
	if (!is_valid)
	{
		write(1, "ERROR!\n", 7);
	}
	return (is_valid);
}

void	display_at(int col, int row, int x, int y)
{
	if ((col == 1 || col == x) && (row == 1 || row == y))
	{
		ft_putchar('o');
	}
	else if (col == 1 || col == x)
	{
		ft_putchar('|');
	}
	else if (row == 1 || row == y)
	{
		ft_putchar('-');
	}
	else
	{
		ft_putchar(' ');
	}
}

void	rush(int x, int y)
{
	int	col;
	int	row;

	if (!check_valid(x, y))
		return ;
	row = 1;
	while (row <= y)
	{
		col = 1;
		while (col <= x)
		{
			display_at(col, row, x, y);
			col++;
		}
		ft_putchar('\n');
		row++;
	}
}
