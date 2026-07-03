/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:22:53 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/04 10:36:23 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalnum(int c)
{
	return ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z')
		|| (c >= 'A' && c <= 'Z'));
}
/*
#include<stdio.h>
int main(void)
{
	int test;
	test = ft_isalnum('c');
	printf("%d", test);
	test = ft_isalnum('0');
	printf("%d", test);
	test = ft_isalnum('\n');
	printf("%d", test);
	test = ft_isalnum(' ');
	printf("%d\n", test);

}
*/