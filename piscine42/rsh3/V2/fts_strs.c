/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fts_strs.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 12:31:07 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/19 12:34:34 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>

char	*ft_atoa(char *number)
{
	char	*nbr;
	int		len;
	char	*temp;

	while (*number < '!')
		number++;
	if (*number != '+' && !(*number >= '0' && *number <= '9'))
		return (NULL);
	else if (*number == '+')
		number++;
	temp = number;
	while (*number >= '0' && *number <= '9')
		number++;
	nbr = malloc((number - temp + 1) * sizeof(char));
	if (!nbr)
		return (NULL);
	len = 0;
	while (*temp >= '0' && *temp <= '9')
		nbr[len++] = *temp++;
	nbr[len] = '\0';
	return (nbr);
}

int	ft_strlen(char *str)
{
	int	len;

	len = 0;
	while (str[len++]);
	return (len - 1);
}

void	putstr(char *str)
{
	int	i;

	i = 0;
	while(str[i])
	{
		write(1, &str[i], 1);
		i ++;
	}
}
