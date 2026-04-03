/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 12:27:26 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/19 12:43:14 by llafforg         ###   ########.fr       */
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

char	*ft_put_word(char **str, char *sep)
{
	char	*word;
	int		len;
	int		i;

	i = 0;
	len = ft_str_length(*str, sep);
	word = malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	while (ft_is_in_sep(**str, sep) != 0 && **str)
	{
		word[i++] = *(*str);
		(*str)++;
	}
	word[len] = '\0';
	return (word);
}

char	**ft_split(char *str, char *sep)
{
	char	**split;
	int		cnt_words;
	int		i;

	cnt_words = ft_ctn_word(str, sep);
	split = malloc(sizeof(char *) * (cnt_words + 1));
	if (!split)
		return (NULL);
	i = 0;
	while (*str)
	{
		while (ft_is_in_sep(*str, sep) == 0)
			str++;
		split[i] = ft_put_word(&str, sep);
		i++;
	}
	split[cnt_words] = NULL;
	return (split);
}
