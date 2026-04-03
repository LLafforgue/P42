/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:56:01 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/24 18:50:32 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdarg.h>

static int	ft_format(char fmt, va_list args, int fd)
{
	if (fmt == '%')
		return (ft_format_char('%', fd));
	if (fmt == 'c')
		return (ft_format_char(va_arg(args, int), fd));
	if (fmt == 'd' || fmt == 'i')
		return (ft_format_signed(va_arg(args, int), fd));
	if (fmt == 'p')
		return (ft_format_ptr(va_arg(args, void *), fd));
	if (fmt == 's')
		return (ft_format_string(va_arg(args, char *), fd));
	if (fmt == 'u')
		return (ft_format_unsigned(va_arg(args, unsigned int), fd));
	if (fmt == 'x')
		return (ft_format_hex(va_arg(args, unsigned int), fd, 0));
	if (fmt == 'X')
		return (ft_format_hex(va_arg(args, unsigned int), fd, 1));
	if (fmt == 'f')
		return (ft_format_double(va_arg(args, double), fd));
	return (0);
}

static int	ft_check_format_str(const char *format)
{
	if (format == NULL)
		return (0);
	while (*format)
	{
		if (*format == '%')
		{
			if (!ft_strchr(ALLOWED_CONVERSIONS, *++format))
				return (0);
		}
		++format;
	}
	return (1);
}

static int	ft_printf_args(int fd, const char *format, va_list args)
{
	int	i;
	int	len;

	i = -1;
	len = 0;
	while (format[++i])
	{
		if (format[i] == '%')
			len += ft_format(format[++i], args, fd);
		else
		{
			ft_putchar_fd(format[i], fd);
			len++;
		}
	}
	return (len);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		len;

	if (!ft_check_format_str(format))
		return (-1);
	va_start(args, format);
	len = ft_printf_args(STDOUT_FILENO, format, args);
	va_end(args);
	return (len);
}

int	ft_printf_err(const char *format, ...)
{
	va_list	args;
	int		len;

	if (!ft_check_format_str(format))
		return (-1);
	va_start(args, format);
	len = ft_printf_args(STDERR_FILENO, format, args);
	va_end(args);
	return (len);
}
