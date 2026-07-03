/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_address.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 13:24:21 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/17 16:48:08 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdio.h>

int	ft_put_address(void *pntr)
{
	unsigned long	addr;
	int				len;
	char			hex[16];
	int				i;

	addr = (unsigned long)pntr;
	len = 0;
	i = 0;
	if (!pntr)
		return ((int)write(1, "(nil)", 5));
	len += write(1, "0x", 2);
	while (addr > 0)
	{
		hex[i++] = "0123456789abcdef"[addr % 16];
		addr /= 16;
	}
	while (i > 0)
		len += write(1, &hex[--i], 1);
	return (len);
}
