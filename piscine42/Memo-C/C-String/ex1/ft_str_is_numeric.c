/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 14:31:55 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 14:47:47 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_numeric(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (*str >= '0' && *str <= '9')
		{
			if (*(str + 1))
				return (ft_str_is_numeric(str + 1));
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
    printf("La '125bla' renvoit %d\n", ft_str_is_numeric("125bla"));
    printf("La '' renvoit %d\n", ft_str_is_numeric(""));
    printf("La '15' renvoit %d\n", ft_str_is_numeric("15"));
    return (0);
}
*/
