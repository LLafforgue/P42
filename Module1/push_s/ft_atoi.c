/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 12:50:21 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/27 15:42:23 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "limits.h"

static int	ft_isspace(char c)
{
	return (c == '\n' || c == '\t' || c == '\f' || c == '\r' || c == '\v'
		|| c == ' ');
}

static const char	*skip_spaces(const char *nptr)
{
	int	i;

	i = 0;
	while (nptr[i])
	{
		if (!ft_isspace(nptr[i]))
			break ;
		i++;
	}
	return (nptr + i);
}

bool	ft_atoi(const char *nptr, int *result)
{
	size_t	i;
	long	sign;
	long	res;
	bool	nb_found;

	nptr = skip_spaces(nptr);
	sign = 1;
	res = 0;
	nb_found = false;
	i = 0;
	if (nptr[i] == '-' || nptr[i] == '+')
	{
		if (nptr[i] == '-')
			sign = -1;
		i++;
	}
	while (nptr[i] && ft_isdigit(nptr[i]))
	{
		res = res * 10 + (nptr[i++] - '0');
		nb_found = true;
		if ((sign > 0 && res > INT_MAX) || (sign < 0 && res - 1 > INT_MAX))
			return (false);
	}
	*result = sign * res;
	return (nb_found);
}
