/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 14:33:29 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/03 14:57:27 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *nptr)
{
	int	nbr;
	int	sign;

	nbr = 0;
	sign = 1;
	while (*nptr == 32 || (*nptr >= '\t' && *nptr <= '\r' ))
		nptr++;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			sign = -1;
		nptr++;
	}
	if (*nptr >= '0' && *nptr <= '9')
	{
		while (*nptr >= '0' && *nptr <= '9')
		{
			nbr *= 10;
			nbr += *nptr - 48;
			nptr++;
		}
		return (nbr * sign);
	}
	return (0);
}
/*
#include<stdio.h>
int main(int argc, char *argv[])
{
	if (argc > 0)
	{
		while (*(++argv))
			printf("result de %s est %d\n", *argv , ft_atoi(*argv));
	}
}
*/
/*
#include<stdio.h>
int main(void)
{
	printf("%d\n", ft_atoi(""));
}
*/