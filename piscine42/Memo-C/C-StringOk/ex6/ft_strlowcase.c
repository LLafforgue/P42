/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 15:39:27 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/09 18:50:04 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

//verification
int	ft_str_has_no_uppercase(char *str)
{
	if (*str == 0)
		return (1);
	else
	{
		if (!(*str >= 'A' && *str <= 'Z'))
		{
			if (*(str + 1))
				return (ft_str_has_no_uppercase(str + 1));
			else
				return (1);
		}
		else
			return (0);
	}
}

char	*ft_strlowcase(char *str)
{
	int	i;

	i = 0;
	if (ft_str_has_no_uppercase(str) == 1)
		return (str);
	else
	{
		while (*(str + i))
		{
			if (*(str + i) >= 'A' && *(str + i) <= 'Z')
				*(str + i) += 32;
			i ++;
		}
		return (str);
	}
}
/*
int main(int argc, char *argv[])
{
    char string[15] = "Il faut un mot\n";
    if (argc != 2)
    {
        printf("%s", ft_strlowcase(string));
        return (1);
    }
    else
    {
        printf("%s devient :\n", *(argv + 1));
        printf("%s\n", ft_strlowcase(*(argv + 1)));
        return (0);
    }
}
*/
