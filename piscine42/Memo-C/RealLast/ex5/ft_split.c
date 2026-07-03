/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 16:40:55 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/23 18:05:23 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_is_in_sep(char c, char *sep)
{
	while (*sep != '\0')
	{
		if (c == *sep || !c)
			return (0);
		sep++;
	}
	return (1);
}

int	ft_ctn_word(char *str, char *sep)
{
	int	cnt;

	cnt = ft_is_in_sep(*str, sep);
	while (*str)
	{
		if (ft_is_in_sep(*str, sep) == 0 && ft_is_in_sep(*(str + 1), sep) == 1)
			cnt++;
		str++;
	}
	return (cnt);
}

int	ft_str_length(char *str, char *sep)
{
	int	len;

	len = 0;
	while (str[len] && ft_is_in_sep(str[len], sep) == 1)
		len ++;
	return (len);
}

char	*ft_put_word(char **str, char *charset)
{
	char	*word;
	int		len;
	int		i;

	i = 0;
	len = ft_str_length(*str, charset);
	word = malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	if (*charset == '\n')
		return (NULL);
	while (ft_is_in_sep(**str, charset) != 0 && **str)
	{
		word[i++] = *(*str);
		(*str)++;
	}
	word[len] = '\0';
	return (word);
}

char	**ft_split(char *str, char *charset)
{
	char	**split;
	int		cnt_words;
	int		i;

	if (!str || !charset)
		return (NULL);
	cnt_words = ft_ctn_word(str, charset);
	split = malloc(sizeof(char *) * (cnt_words + 1));
	if (!split)
		return (NULL);
	i = 0;
	while (*str)
	{
		while (ft_is_in_sep(*str, charset) == 0)
			str++;
		split[i] = ft_put_word(&str, charset);
		i++;
	}
	split[cnt_words] = NULL;
	return (split);
}
/*
#include <stdio.h>
int	main(void)
{
    char *str = "LW.2t/V3.TXXG9ZO+evG[DVD)";
    char *sep = ").GXS";
    char **split = ft_split(str, sep);

    while (*split != NULL)
    {
        printf("mot :%s\n", *split);
        split++;
    }
}
*/