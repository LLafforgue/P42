/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 17:17:04 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/03 17:19:32 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	else
		return (c);
}
// 
// #include <stdio.h>
// #include <ctype.h>
// int main()
// {
//     char c, result;

//     c = 'M';
//     result = ft_tolower(c);
//     printf("tolower(%c) = %c\n", c, result);

//     c = 'm';
//     result = ft_tolower(c);
//     printf("tolower(%c) = %c\n", c, result);

//     c = '+';
//     result = ft_tolower(c);
//     printf("tolower(%c) = %c\n", c, result);

//     return 0;
// }