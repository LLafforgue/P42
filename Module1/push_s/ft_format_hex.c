/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_hex.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:59:37 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/17 17:36:46 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_format_hex(unsigned int x, int fd, int is_upper)
{
	size_t	len;

	len = 0;
	if (x >= 16)
		len = ft_format_hex(x / 16, fd, is_upper);
	if (is_upper)
		ft_putchar_fd(HEX_UPPER[x % 16], fd);
	else
		ft_putchar_fd(HEX[x % 16], fd);
	return (++len);
}
