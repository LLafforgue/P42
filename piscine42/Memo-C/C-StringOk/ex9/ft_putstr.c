/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 16:56:49 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/13 10:55:16 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr(char *str)
{
	if (*str == '\0')
		return ;
	write(1, &*str, 1);
	ft_putstr(str + 1);
}
/*
int main()
{
    ft_putstr("");
    ft_putstr("\n");
    ft_putstr("Oups\n");

    return (0);
}
*/
