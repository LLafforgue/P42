/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 14:37:42 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 14:48:22 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_printable(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (*str >= 32 && *str <= 126)
		{
			if (*(str + 1))
				return (ft_str_is_printable(str + 1));
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
    printf("La '125bla' renvoit %d\n", ft_str_is_printable("125bla"));
    printf("La 'BOU' renvoit %d\n", ft_str_is_printable("BOU"));
    printf("La 'BouBa\\n' renvoit %d\n", ft_str_is_printable("BouBa\n"));
    return (0);
}
*/
