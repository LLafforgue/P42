/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format_signed.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:59:37 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/17 17:36:03 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

size_t	ft_format_signed(int i, int fd)
{
	size_t	len;
	long	li;

	len = 0;
	li = i;
	if (li < 0)
	{
		ft_putchar_fd('-', fd);
		li = -li;
		len++;
	}
	if (li >= 10)
		len += ft_format_signed(li / 10, fd);
	ft_putchar_fd(li % 10 + '0', fd);
	return (++len);
}
