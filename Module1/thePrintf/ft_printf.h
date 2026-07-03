/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 15:11:11 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/17 16:54:41 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	ft_put_str(char *s);
int	ft_put_nbr(int n);
int	ft_put_address(void *pntr);
int	ft_put_unsigned_hex(unsigned int n, int s);
int	ft_put_unsigned_nbr(unsigned int n);
int	ft_printf(const char *format, ...);

#endif
