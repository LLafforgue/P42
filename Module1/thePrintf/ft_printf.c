/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 16:59:41 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/20 19:37:39 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_check_format(char f)
{
	if (f != 'd' && f != 'i' && f != 'u' && f != 'x' && f != 'X' && f != '%'
		&& f != 'p' && f != 's' && f != 'c')
		return (0);
	return (1);
}

void	ft_put_format(char f, int *len, va_list args)
{
	if (f == 'd' || f == 'i')
		*len += ft_put_nbr(va_arg(args, int));
	if (f == 'u')
		*len += ft_put_unsigned_nbr(va_arg(args, int));
	if (f == 'c')
		*len += write(1, (char [1]){(char)va_arg(args, int)}, 1);
	if (f == '%')
		*len += write(1, &f, 1);
	if (f == 's')
		*len += ft_put_str(va_arg(args, char *));
	if (f == 'p')
		*len += ft_put_address(va_arg(args, void *));
	if (f == 'x')
		*len += ft_put_unsigned_hex(va_arg(args, unsigned int), (int) 0);
	if (f == 'X')
		*len += ft_put_unsigned_hex(va_arg(args, unsigned int), (int) 1);
}

const char	*ft_pass(const char **format)
{
	(*format)++;
	while (**format == ' ')
		(*format)++;
	return (*format);
}

int	ft_error(const char *format)
{
	if (!format)
		return (-1);
	while (*format)
	{
		if (*format == '%' && !ft_check_format(*ft_pass(&format)))
			return (1);
		format++;
	}
	return (0);
}

int	ft_printf(const char *format, ...)
{
	int			len;
	va_list		args;

	len = 0;
	va_start(args, format);
	if (ft_error(format))
		return (-1);
	while (*format)
	{
		while (*format && *format != '%')
			len += write(1, format++, 1);
		if (*format == '%')
		{
			ft_put_format(*(format + 1), &len, args);
			format += 2;
		}
	}
	return (len);
}

#include <stdio.h>
int main ()
{
	ft_printf("%p\n", -2147483648);
	printf("%p", -2147483648);
}
//gcc ft_printf.c ft_printf.h ft_put_address.c ft_put_nbr.c ft_put_str.c ft_put_unsigned_hex.c ft_put_unsigned_nbr.c -o test -Wall -Wextra -Werror