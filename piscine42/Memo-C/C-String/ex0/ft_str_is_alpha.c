/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 14:24:48 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 14:47:54 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_alpha(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if ((*str >= 'A' && *str <= 'Z') || (*str >= 'a' && *str <= 'z'))
		{
			if (*(str + 1))
				return (ft_str_is_alpha(str + 1));
			else
				return (1);
		}
		else
			return (0);
	}
}

/*
#include<stdio.h>

int main(void)
{
    printf("La 'Bla&bla' renvoit %d\n", ft_str_is_alpha("Bla&bla"));
    printf("La  '' renvoit %d\n", ft_str_is_alpha(""));
    printf("La 'Ok' renvoit %d\n", ft_str_is_alpha("Ok"));
    return (0);
}
*/
