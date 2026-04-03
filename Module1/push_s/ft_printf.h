/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: osasburg <olivier.sasburg@learner.42.te    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:49:52 by osasburg          #+#    #+#             */
/*   Updated: 2025/11/24 18:50:39 by osasburg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include "libft.h"

# define NULL_RES "(null)"
# define NULL_LEN 6

# define NIL_RES "(nil)"
# define NIL_LEN 5

# define PTR_PREFIX "0x"
# define PTR_PREFIX_LEN 2

# define HEX "0123456789abcdef"
# define HEX_UPPER "0123456789ABCDEF"

# define ALLOWED_CONVERSIONS "cspdiuxX%f"

int		ft_printf(const char *format, ...);
int		ft_printf_err(const char *format, ...);

size_t	ft_format_char(char c, int fd);
size_t	ft_format_double(double d, int fd);
size_t	ft_format_hex(unsigned int x, int fd, int is_upper);
size_t	ft_format_ptr(void *ptr, int fd);
size_t	ft_format_signed(int i, int fd);
size_t	ft_format_string(char *s, int fd);
size_t	ft_format_unsigned(unsigned int u, int fd);

#endif
