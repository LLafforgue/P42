/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 13:55:06 by smlamali          #+#    #+#             */
/*   Updated: 2026/02/27 17:33:28 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// Write a string in a given file directory
void	ft_putstr(char *str, int fd)
{
	if (!str)
		return ;
	while (*str)
		write(fd, str++, 1);
}

//get len to malloc for ft_itoa
static int	len_nbr(int nbr)
{
	int	i;

	i = 0;
	if (nbr <= 0)
	{
		nbr = -nbr;
		i++;
	}
	while (nbr > 0)
	{
		nbr = nbr / 10;
		i++;
	}
	return (i);
}

static void	reverse_str(char *str)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	j = 0;
	while (str[j])
		j++;
	j--;
	if (!str)
		return ;
	if (str[i] == '-')
		i++;
	while (str[i] && i < j)
	{
		tmp = str[i];
		str[i] = str[j];
		str[j] = tmp;
		i++;
		j--;
	}
}

//utils to print elements in stack (with ft_lstprint)
char	*ft_itoa(int nbr)
{
	int		i;
	char	*str;

	i = 0;
	str = NULL;
	str = malloc(sizeof(int) * (len_nbr(nbr) + 1));
	if (!str)
		return (NULL);
	if (nbr == 0)
		str[i++] = '0';
	if (nbr < 0)
	{
		str[i++] = '-';
		nbr = -nbr;
	}
	while (nbr > 0)
	{
		str[i++] = nbr % 10 + '0';
		nbr = nbr / 10;
	}
	str[i] = '\0';
	reverse_str(str);
	return (str);
}

int	ft_atoi(char *str)
{
	int	i;
	int	sign;
	int	number;

	i = 0;
	sign = 1;
	number = 0;
	if (!str || !*str || *str == '0')
		return (0);
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		if (number > number * 10 + (str[i] - '0'))
			return (2147483647);
		number = number * 10 + (str[i] - '0');
		i++;
	}
	return (number * sign);
}
