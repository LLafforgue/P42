/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_lowercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 15:02:03 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 15:33:37 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_lowercase(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (*str >= 'a' && *str <= 'z')
		{
			if (*(str + 1))
				return (ft_str_is_lowercase(str + 1));
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
    printf("La '125bla' renvoit %d\n", ft_str_is_lowercase("125bla"));
    printf("La 'ok' renvoit %d\n", ft_str_is_lowercase("ok"));
    printf("La 'BouBa' renvoit %d\n", ft_str_is_lowercase("BouBa"));
    return (0);
}
*/
