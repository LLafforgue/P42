/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 12:23:59 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/19 20:24:16 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include "rush_02.h"
#include "lib/rs.h"

void	ft_print_one_order(char **dict_p, char *nbr, int x, int n)
{
	int	i;

	i = 0;
	while (dict_p[i])
	{
		if ((x - 1) / 3 == (ft_strlen(dict_p[i]) - 1) / 3
			&& nbr[n - x] != '0')
		{
			ft_print_cdu(dict_p, nbr + (n - x), x % 3);
			ft_putstr(dict_p[i + 1]);
			return ;
		}
		i += 2;
	}
}

void	print_explore_number(char **dict_p, char *nbr)
{
	int	i;
	int	x;
	int	n;

	i = 0;
	n = ft_strlen(nbr);
	x = n;
	while (x > 2 && dict_p[i])
	{
		if (x <= 3)
		{
			ft_print_cdu(dict_p, nbr, x % 3);
			return ;
		}
		ft_print_one_order(dict_p, nbr, x, n);
		x--;
	}
}

void	ft_write_number(const char *dict, char *number)
{
	char	**dict_p;
	int		i;

	i = 0;
	if (*dict)
	{
		dict_p = ft_parse_lib(dict);
		if (ft_strlen(number) == 2)
			def_dec(dict_p, number);
		else
			print_explore_number(dict_p, number);
		write(1, "\n", 1);
		i = 0;
		while (dict_p[i] != NULL)
			free(dict_p[i++]);
		free(dict_p);
	}
	else
		write(1, "Error\n", 7);
}

int	main(int argc, char *argv[])
{
	char		*number;
	const char	*dict;

	if (argc != 2 && argc != 3)
		write(1, "Error\n", 6);
	else
	{
		number = ft_atoa(argv[argc - 1]);
		if (number == NULL)
		{
			write(1, "Error\n", 6);
			return (1);
		}
		if (argc == 2)
			dict = "./numbers.dict";
		if (argc == 3)
			dict = argv[1];
	}
	ft_write_number(dict, number);
}
