/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_parse_all.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 12:35:12 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/19 12:37:38 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include "ft_split.h"

// Recuperer la taille totale du document en octet (char)
int	ft_explore_dict(const char *dict)
{
	int		nb;
	char	buff[1024];
	int		fd;
	int		nb_acc;

	fd = open(dict, O_RDONLY);
	if (fd == -1)
		return (0);
	nb = 1;
	while (nb != 0)
	{
		nb = read(fd, buff, 1);
		nb_acc += nb;
	}
	close(fd);
	return (nb_acc);
}

char	**ft_parse_lib(const char *dict)
{
	int		fd;
	char	*dict_p;
	char	**dict_num_car;
	int		nb_acc;

	nb_acc = ft_explore_dict(dict);
	if (nb_acc == 0)
		return (NULL);
	dict_p = malloc(sizeof(char) * (nb_acc + 1));
	if (!dict_p)
		return (NULL);
	fd = open(dict, O_RDONLY);
	read(fd, dict_p, nb_acc);
	close(fd);
	dict_p[nb_acc] = '\0';
	dict_num_car = ft_split(dict_p, " :\n");
	return (dict_num_car);
}
