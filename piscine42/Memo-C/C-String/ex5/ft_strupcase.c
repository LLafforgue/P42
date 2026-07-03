/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 15:39:27 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 17:04:56 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

//verification
int	ft_str_has_no_lowercase(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (!(*str >= 'a' && *str <= 'z'))
		{
			if (*(str + 1))
				return (ft_str_has_no_lowercase(str + 1));
			else
				return (1);
		}
		else
			return (0);
	}
}

char	*ft_strupcase(char *str)
{
	int	i;

	i = 0;
	if (ft_str_has_no_lowercase(str) == 1)
		return (str);
	else
	{
		while (*(str + i))
		{
			if (*(str + i) >= 'a' && *(str + i) <= 'z')
				*(str + i) -= 32;
			i ++;
		}
		return (str);
	}
}
/*
int	main(int argc, char *argv[])
{
	char	string[15] = "Il faut un mot\n";
	if (argc != 2)
    {
        printf("%s", ft_strupcase(string));
        return (1);
    }
    else
    {
        printf("%s devient :\n", *(argv + 1));
        printf("%s\n", ft_strupcase(*(argv + 1)));
        return (0);
    }
}
*/
