/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/05 14:32:13 by llafforg          #+#    #+#             */
/*   Updated: 2025/11/05 14:33:51 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

static int	ft_is_sep(char c, char sep)
{
	if (c == sep)
		return (1);
	return (0);
}

static int	ft_cnt_word(const char *str, char c)
{
	int	cnt;

	cnt = 0;
	while (*str)
	{
		while (*str && *str == c)
			str++;
		if (*str)
		{
			cnt++;
			while (*str && *str != c)
				str++;
		}
	}
	return (cnt);
}

static char	*ft_strdup(const char **str, char c)
{
	char	*dup;
	char	*temp;

	temp = (char *)*str;
	while (**str && !ft_is_sep(**str, c))
		(*str)++;
	dup = malloc(sizeof(char) * ((*str) - temp + 1));
	if (!dup)
		return (NULL);
	*str = temp;
	temp = dup;
	while (**str && !ft_is_sep(**str, c))
	{
		*dup++ = **str;
		(*str)++;
	}
	*dup = '\0';
	return (temp);
}

char	**ft_split(const char *s, char c)
{
	char	**split;
	int		len;

	if (!s)
		return (NULL);
	len = ft_cnt_word(s, c);
	split = malloc(sizeof(char *) * (len + 1));
	if (!split)
		return (NULL);
	len = 0;
	while (*s)
	{
		while (ft_is_sep(*s, c))
			s++;
		if (*s)
			split[len++] = ft_strdup(&s, c);
	}
	split[len] = NULL;
	return (split);
}
/*
#include <stdio.h>
int main(void)
{
	char * * tab = ft_split("", ' ');
	int i = 0;
	while(tab[i])
		printf("%s\n", tab[i++]);
	printf("%d\n", i);
	printf("%p\n", tab[i]);
	while(i >= 0)
		free(tab[i--]);
	free(tab);
}
*/
