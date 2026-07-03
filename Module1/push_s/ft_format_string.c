/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_string.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 16:44:39 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/17 17:37:18 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_format_string(char *s, int fd)
{
	if (s)
	{
		ft_putstr_fd(s, fd);
		return (ft_strlen(s));
	}
	ft_putstr_fd(NULL_RES, fd);
	return (NULL_LEN);
}
