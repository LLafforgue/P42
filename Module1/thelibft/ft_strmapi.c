/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 17:35:32 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/05 17:35:33 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	index;
	size_t			len;
	char			*nstr;
	char			*temp;

	if (!s || !f)
		return (NULL);
	len = ft_strlen(s);
	nstr = malloc((len + 1) * sizeof(char));
	if (!nstr)
		return (NULL);
	temp = nstr;
	index = 0;
	while (*s)
	{
		*nstr++ = f(index, *s);
		s++;
		index++;
	}
	*nstr = '\0';
	return (temp);
}
/*
char ft_test(unsigned int index, char c)
{
    return (c + index);
}

#include <stdio.h>
int main(void)
{
    char const *s = "Hdjik !";
    char *test = ft_strmapi(s, &ft_test);
    printf("%s\n", test);
}
*/
