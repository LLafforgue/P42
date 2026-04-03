/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 16:43:36 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/10 12:23:42 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_verif(char *str)
{
	if (!(*str >= 'a' && *str <= 'z'))
	{
		if (!(*str >= '0' && *str <= '9'))
		{
			if (!(*str >= 'A' && *str <= 'Z'))
			{
				if (*(str + 1) >= 'a' && *(str + 1) <= 'z')
					return (0);
			}
		}
	}
	return (1);
}

//tout mettre lowercase
void	ft_strlowercase(char *str)
{
	int	i;

	i = 0;
	while (*(str + i))
	{
		if (*(str + i) >= 'A' && *(str + i) <= 'Z')
			*(str + i) += 32;
		i ++;
	}
}

char	*ft_strcapitalize(char *str)
{
	int	j;

	j = 0;
	if (*str == 0)
		return (str);
	else
	{
		ft_strlowercase(str);
		if (*str && *str >= 'a' && *str <= 'z')
			*str -= 32;
		while (*(str + j))
		{
			if (ft_verif(str + j) == 0)
				*(str + j + 1) -= 32;
			j ++;
		}
		return (str);
	}
}
/*
#include<stdio.h>

int main(int argc, char *argv[])
{
    char string[15] = "Il faut un mot";
    if (argc != 2)
    {
        printf("%s", ft_strcapitalize(string));
        return (1);
    }
    else
    {
        printf("%s devient :\n", *(argv + 1));
        printf("%s\n", ft_strcapitalize(*(argv + 1)));
        return (0);
    }
}
*/
