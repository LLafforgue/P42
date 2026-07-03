/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_unsigned.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:59:37 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/17 17:35:52 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_format_unsigned(unsigned int u, int fd)
{
	size_t	len;

	len = 0;
	if (u >= 10)
		len = ft_format_unsigned(u / 10, fd);
	ft_putchar_fd(u % 10 + '0', fd);
	return (++len);
}
