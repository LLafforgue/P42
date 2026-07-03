/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_ptr.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:59:37 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/17 17:29:48 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static size_t	ft_putxlnbr_fd(unsigned long x, int fd)
{
	size_t	len;

	len = 0;
	if (x >= 16)
		len = ft_putxlnbr_fd(x / 16, fd);
	ft_putchar_fd(HEX[x % 16], fd);
	return (++len);
}

size_t	ft_format_ptr(void *ptr, int fd)
{
	if (ptr == NULL)
	{
		ft_putstr_fd(NIL_RES, fd);
		return (NIL_LEN);
	}
	ft_putstr_fd(PTR_PREFIX, fd);
	return (PTR_PREFIX_LEN + ft_putxlnbr_fd((unsigned long)ptr, fd));
}
