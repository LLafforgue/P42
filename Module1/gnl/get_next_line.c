/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 10:55:54 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/20 17:53:39 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>
#include <fcntl.h>

int	ft_size_join(int len, char *buff, char	*str)
{
	int		i;

	i = 0;
	while (i < len && buff[i] != SEPARATOR)
		i++;
	i += buff[i] == SEPARATOR;
	return (i + ft_strlen(str) + 1);
}

int	ft_join(char *buff, char **str, int len)
{
	char	*temp;
	char	*copy;
	char	*join;
	int		i;

	copy = *str;
	join = malloc(sizeof(char) * ft_size_join(len, buff, copy));
	if (!join)
		return (0);
	temp = join;
	i = 0;
	while (*copy)
		*join++ = *copy++;
	while (i < len && buff[i] != SEPARATOR)
		*join++ = buff[i++];
	if (buff[i] == SEPARATOR)
		*join++ = buff[i++];
	*join = '\0';
	copy = *str;
	*str = temp;
	free(copy);
	return (i);
}

char	*get_next_line(int fd)
{
	static int	i = 0; //position dans buff
	static int	read_size = 0;
	static char	buff[BUFFER_SIZE + 1] = {0};
	char		*str;

	str = ft_calloc_empty(1);
	while (!ft_chek_line(str))
	{
		if (i < read_size)
			i += ft_join(buff + i, &str, read_size - i);
		else
		{
			read_size = read(fd, buff, BUFFER_SIZE);
			if (!*buff || read_size == -1)
				return (ft_error(str));
			buff[read_size] = 0;
			i = ft_join(buff, &str, read_size);
			if (!read_size && (!*str || *str == SEPARATOR))
				return (ft_error(str));
			if (!read_size && *str)
				return (str);
		}
	}
	return (str);
}

/* int	main(void)
{
	int		fd;
	int		cnt;
	int		deb;
	char	*line;

	deb = 0;
	cnt = 6;
	fd = open("./test", O_RDONLY);
	while (deb < cnt)
	{
		line = get_next_line(fd);
		printf("l%d : %s-----\n", deb + 1, line);
		deb++;
		free(line);
	}
	close(fd);
}  */
// cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c get_next_line.h -D BUFFER_SIZE=42