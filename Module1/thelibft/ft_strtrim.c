/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 15:32:47 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/05 15:32:50 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

static int	ft_is_a_set(char c, char const *set)
{
	while (*set)
		if (*set++ == c)
			return (1);
	return (0);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*trim;
	size_t	start;
	size_t	end;
	size_t	len;

	if (!s1)
		return (NULL);
	start = 0;
	while (ft_is_a_set(s1[start], set) && s1[start])
		start++;
	end = start;
	while (s1[end])
		end++;
	end--;
	while (ft_is_a_set(s1[end], set) && end > start)
		end--;
	len = end - start + 1;
	trim = malloc((len + 1) * sizeof(char));
	if (!trim)
		return (NULL);
	end = 0;
	while (end < len)
		trim[end++] = s1[start++];
	trim[end] = '\0';
	return (trim);
}
/*
#include <stdio.h>
int main(void)
{
	char		*trim = ft_strtrim("llllloL!loooLol" , "loL");
	printf("%s\n", trim);
	free(trim);
	trim = ft_strtrim("llllloL!loooLolil" , "loL");
	printf("%s\n", trim);
	free(trim);
	trim = ft_strtrim("" , "loL");
	printf("%s\n", trim);
	free(trim);
}
*/