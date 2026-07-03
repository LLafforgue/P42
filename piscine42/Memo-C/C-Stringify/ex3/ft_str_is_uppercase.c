/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 15:06:25 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 15:36:52 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_uppercase(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (*str >= 'A' && *str <= 'Z')
		{
			if (*(str + 1))
				return (ft_str_is_uppercase(str + 1));
			else
				return (1);
		}
		else
			return (0);
	}
}

/*
include<stdio.h>
int main(void)
{
    printf("'125bla' renvoit %d\n", ft_str_is_uppercase("125bla"));
    printf("'OK' renvoit %d\n", ft_str_is_uppercase("OK"));
    printf("'BouBa' renvoit %d\n", ft_str_is_uppercase("BouBa"));
    return (0);
}
*/
