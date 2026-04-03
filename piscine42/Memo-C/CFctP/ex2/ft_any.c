/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_any.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 19:02:44 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 16:31:41 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_any(char **tab, int (*f)(char*))
{
	int	i;

	i = 0;
	while (tab[i])
	{
		if (f(tab[i]) == 1)
			return (1);
		i++;
	}
	return (0);
}
/*
int f_test(char *tab)
{
    int i = 0;
    while (tab[i])
    {
        if(tab[i] == ' ')
            return (1);
        i++;
    }
    return (0);
}

int main(void)
{
    char *tab[3];
    tab[0] = "ok";
    tab[1] = "pasok";
    tab[2] = 0;
    int resp;

    resp = ft_any(tab, &f_test);
    printf(" %d", resp);
    return (0);
}
*/
