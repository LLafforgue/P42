/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/09 14:37:42 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/03 17:00:06 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

void	*ft_memset(void *buff, int c, size_t n)
{
	unsigned char	*loc;

	loc = buff;
	while (n > 0)
		loc[--n] = (unsigned char)c;
	return (buff);
}
// 
// int main( void )
// {
//    char buffer[38] = "This is a test of the memset function";

//    printf( "Before: %s\n", buffer );
//    memset( buffer, '*', 4 );
//    printf( "After:  %s\n", buffer );
// }
