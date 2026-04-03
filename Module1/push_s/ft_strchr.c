/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 15:32:25 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/09 15:39:37 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	int		i;
	int		len;
	char	chr;

	chr = c;
	len = ft_strlen(s);
	i = -1;
	while (++i <= len)
		if (s[i] == chr)
			return ((char *)(s + i));
	return (NULL);
}
