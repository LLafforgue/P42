/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:03:44 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 13:45:52 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_is_sort(int *tab, int length, int (*f)(int, int))
{
	int	i;
	int	start;

	i = 1;
	if (length < 3)
		return (1);
	start = f(tab[0], tab[1]);
	while (i + 1 < length)
	{
		if (start != 0 && f(tab[i], tab[i + 1]) != 0)
		{
			if (start * f(tab[i], tab[i + 1]) < 0)
				return (0);
		}
		else if (f(tab[i], tab[i + 1]) != 0)
			start = f(tab[i], tab[i + 1]);
		i ++;
	}
	return (1);
}
/*
int ft_test(int a, int b)
{
    return (a - b);
}

int main(void)
{
    int res;
    int test[5] = {5, 2, 2, 2, 2};
    res = ft_is_sort(test, 5, &ft_test);
    printf("%d", res);
}
*/
