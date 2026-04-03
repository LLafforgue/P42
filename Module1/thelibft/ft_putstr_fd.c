/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 16:15:03 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/12 16:15:05 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr_fd(char *s, int fd)
{
	char	*temp;

	if (s)
	{
		temp = s;
		while (*s)
			s++;
		write(fd, temp, s - temp);
	}
}
/*
int main(void)
{
    char *s = "Avadaaaa!";

    ft_putstr_fd(s, 0);
    write(1, "\n", 1);
    ft_putstr_fd((void *)0, 0);
    write(1, "\n", 1);
}
*/
