/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 15:09:40 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/22 16:17:06 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr(char *str)
{
	if (*str == '\0')
		return ;
	write(1, str, 1);
	ft_putstr(str + 1);
}

int	ft_compare_w(char *w1, char *w2)
{
	while (*w1 && *w2)
	{
		if (*w1 > *w2)
			return (-1);
		if (*w1 == *w2)
		{
			w1++;
			w2++;
		}
		if (*w1 < *w2)
			return (1);
	}
	if (*w2 || (!*w2 && !*w1))
		return (0);
	else
		return (-1);
}

void	ft_sort_argv(char **tab, int size)
{
	char	*min;
	int		i;

	if (size <= 1)
		return ;
	i = 1;
	min = *tab;
	while (i < size)
	{
		if (ft_compare_w(*tab, tab[i]) == -1)
		{
			min = tab[i];
			tab[i] = *tab;
			*tab = min;
		}
		i ++;
	}
	ft_sort_argv(tab + 1, size - 1);
}

int	 main(int argc, char *argv[])
{
	int i;

	argv++;
	ft_sort_argv(argv, argc - 1);
	i = 0;
	while (argv[i])
	{
		ft_putstr(argv[i]);
		write(1, "\n", 1);
		i++;
	}
	return (0);
}

