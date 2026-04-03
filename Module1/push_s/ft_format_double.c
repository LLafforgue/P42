/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_double.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:59:37 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/24 18:51:43 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_format_double(double d, int fd)
{
	size_t	len;

	len = ft_format_signed((int)d, fd);
	ft_putchar_fd('.', fd);
	len += ft_format_signed((int)(d * 10) % 10, fd);
	len += ft_format_signed((int)(d * 100) % 10, fd);
	return (++len);
}
