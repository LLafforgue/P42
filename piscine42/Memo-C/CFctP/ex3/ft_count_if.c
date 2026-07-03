/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_if.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:03:15 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 13:47:07 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_count_if(char **tab, int length, int (*f)(char*))
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (i < length)
	{
		if (f(tab[i]) != 0)
			count ++;
		i ++;
	}
	return (count);
}
/*
int f_test(char *tab)
{
    int i = 0;
    while (tab[i])
    {
        if(tab[i] == ' ')
            return (1);
        printf("%c", tab[i]);
        i++;
    }
    return (0);
}

int main(void)
{
    char *tab[3];
    tab[0] = "ok";
    tab[1] = "pas ok";
    tab[2] = " ";

    int resp;

    resp = ft_count_if(tab, 3, &f_test);
    printf("%d", resp);
    return (0);
}
*/
