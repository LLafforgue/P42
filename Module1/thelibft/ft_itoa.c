/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 17:07:59 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/05 17:08:00 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#define INT_MIN -2147483648

static int	ft_is_neg(int *n)
{
	if (*n < 0)
	{
		if (*n == INT_MIN)
			return (-1);
		*n *= -1;
		return (1);
	}
	return (0);
}

static char	*ft_int_min(void)
{
	char	*toa;
	char	*min;
	char	*temp;

	min = "-2147483648";
	toa = malloc(sizeof(char) * 12);
	if (!toa)
		return (NULL);
	temp = toa;
	while (*min)
		*toa++ = *min++;
	*toa = '\0';
	return (temp);
}

static char	*ft_print_toa(int n, size_t len)
{
	char	*toa;

	toa = malloc(sizeof(char) * (len + 1));
	if (!toa)
		return (NULL);
	toa[len--] = '\0';
	if (!n)
		*toa = '0';
	else
	{
		while (n > 0)
		{
			toa[len--] = n % 10 + '0';
			n /= 10;
		}
	}
	return (toa);
}

char	*ft_itoa(int n)
{
	size_t	len;
	int		nbis;
	int		neg;
	char	*toa;

	len = (n < 0 || n == 0);
	neg = ft_is_neg(&n);
	if (neg == -1)
		return (ft_int_min());
	nbis = n;
	while (n > 0)
	{
		n /= 10;
		len++;
	}
	toa = ft_print_toa(nbis, len);
	if (neg)
		*toa = '-';
	return (toa);
}
/*

#include <stdio.h>
int main(void)
{
	char *test;

	int test1 = 1959552;
	test = ft_itoa(test1);
	printf("test1 :%s\n", test);
	free(test);
	int test2 = -2;
	test = ft_itoa(test2);
	printf("test2 :%s\n", test);
	free(test);
	int test3 = -2147483648;
	test = ft_itoa(test3);
	printf("test3 :%s\n", test);
	free(test);
	int test4 = 0;
	test = ft_itoa(test4);
	printf("test4 :%s\n", test);
	free(test);
}
*/
