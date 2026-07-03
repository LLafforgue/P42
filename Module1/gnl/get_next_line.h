/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 10:56:02 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/20 13:04:33 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <unistd.h>
# include <stdlib.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif
# ifndef SEPARATOR
#  define SEPARATOR '\n'
# endif

char	*get_next_line(int fd);
int		ft_strlen(char *s);
void	*ft_calloc_empty(size_t size);
int		ft_chek_line(char *str);
void	*ft_error(char *str);

#endif
