/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 13:21:29 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 13:36:32 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
#include <stdio.h>
void ft_print(int *buff, int size)
{
    if (size == 0)
        return ;
    printf("%d\n", *buff);
    return ft_print(buff + 1, size-1);
}
*/
void	ft_sort_int_tab(int *tab, int size)
{
	int	min;
	int	i;

	if (size <= 1)
		return ;
	i = 1;
	min = *tab;
	while (i < size)
	{
		if (min > *(tab + i))
		{
			min = *(tab + i);
			*(tab + i) = *tab;
			*tab = min;
		}
		i ++;
	}
	ft_sort_int_tab(tab + 1, size - 1);
}
/*
int main(void)
{
    int tab[6] = {4, 2, 4, 2, 8, 4};
    ft_sort_int_tab(tab, 6);
    ft_print(tab, 6);
}
*/
