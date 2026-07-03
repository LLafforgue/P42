/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 17:15:47 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/09 18:00:55 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_alloc(int n)
{
	size_t	length;
	int		sign;

	length = 0;
	sign = 0;
	if (n < 0)
		sign = 1;
	while (n)
	{
		n /= 10;
		length++;
	}
	if (length == 0)
		length = 1;
	return (ft_calloc(length + sign + 1, sizeof(char)));
}

static char	*ft_putdigit(int n, char *str)
{
	if (n >= 10 || n <= -10)
		str = ft_putdigit(n / 10, str) + 1;
	n %= 10;
	if (n < 0)
		n = -n;
	str[0] = n + '0';
	return (str);
}

char	*ft_itoa(int n)
{
	char	*str;
	size_t	i;

	str = ft_alloc(n);
	if (str)
	{
		i = 0;
		if (n < 0)
			str[i++] = '-';
		ft_putdigit(n, str + i);
	}
	return (str);
}
