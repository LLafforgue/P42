/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 14:06:09 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/03 15:07:45 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

size_t	ft_strlen(const char *str)
{
	const char	*s;

	s = str;
	while (*str)
		str++;
	return (str - s);
}
// #include <stdio.h>
// int main(void)
// {
// 	size_t len = ft_strlen("Hello!");
// 	printf("%ld", len);
// }
