/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 14:23:28 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 09:51:17 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalpha(int c)
{
	return ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'));
}
/*
#include <stdio.h>
int main(void)
{
	int test;
	test = ft_isalpha('c');
	printf("%d", test);
	test = ft_isalpha('a');
	printf("%d", test);
	test = ft_isalpha('Q');
	printf("%d", test);
	test = ft_isalpha('+');
	printf("%d\n", test);
}
*/
