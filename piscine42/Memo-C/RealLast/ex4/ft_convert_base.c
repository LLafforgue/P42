/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 15:04:28 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/22 22:11:14 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_str_len(char *str);

int	ft_check_base(char *base)
{
	char	*check;
	int		i;

	i = 0;
	check = base;
	if (base[0] != '\0' && base[1] != '\0'
		&& base[0] != '+' && base[0] != '-' && base[0] > ' ' && base[0] != 127)
	{
		while (*check != '\0')
		{
			while (base[++i] != '\0')
			{
				if (base[i] == *check
					|| base[i] == '+' || base[i] == '-' || base[i] <= ' ')
					return (0);
			}
			check++;
			base = check;
			i = 0;
		}
	}
	else
		return (0);
	return (1);
}

int	ft_is_in_base(char nbr, char *base)
{
	while (nbr != *base)
	{
		base++;
		if (*base == '\0')
			return (0);
	}
	return (1);
}

int	ft_base_to_dec(char *nbr, char *base, int mod)
{
	int	number;
	int	i;
	int	neg;

	neg = 1;
	while (ft_is_in_base(*nbr, base) == 0)
	{
		if (*nbr == '-')
			neg *= -1;
		nbr++;
	}
	i = 0;
	number = 0;
	while (ft_is_in_base(*nbr, base) == 1)
	{
		number *= mod;
		while (*nbr != base[i])
			i++;
		number += i;
		i = 0;
		nbr++;
	}
	if (neg < 0)
		number = -number;
	return (number);
}

char	*ft_dec_to_base(int *nbr, char *base, int size, int mod)
{
	char	*conv;
	int		nb;

	nb = *nbr;
	if (nb < 0)
	{
		size++;
		nb = -nb;
	}
	conv = malloc((size + 1) * sizeof(char));
	if (!conv)
		return (NULL);
	conv[size] = '\0';
	while (nb > 0)
	{
		conv[--size] = base[nb % mod];
		nb /= mod;
	}
	if (*nbr < 0)
		conv[0] = '-';
	return (conv);
}

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	int	mod;
	int	number;
	int	n;
	int	i;

	if (ft_check_base(base_from) == 0 || ft_check_base(base_to) == 0)
		return (NULL);
	if (!nbr)
		return (NULL);
	mod = ft_str_len(base_from);
	number = ft_base_to_dec(nbr, base_from, mod);
	mod = ft_str_len(base_to);
	n = number;
	i = 0;
	while (n != 0)
	{
		n /= mod;
		i ++;
	}
	return (ft_dec_to_base(&number, base_to, i, mod));
}
/*
#include <stdio.h>
int	main(void)
{
	char	*base_f = "0123456789";
	char	*base_t = "abcdexghij";
	char	*nbr = "  	-----51coucou";
	char	*res;

	printf("Base From : %d\n", ft_check_base(base_f));
	res = ft_convert_base(nbr, base_f, base_t);
	if (res)
	{
		printf("%s\n", res);
		if (*res)
			free(res);
	}
	return (0);
}
*/
