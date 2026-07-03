/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush_02.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: llafforg <llafforg@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 12:38:28 by llafforg          #+#    #+#             */
/*   Updated: 2025/10/19 12:44:55 by llafforg         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef RUSH_02_H
# define RUSH_02_H

char	    *ft_atoa(char *number);
int		    ft_strlen(char *str);
char	    **ft_parse_lib(const char *dict);
void	    putstr(char *str);
void	ft_print_cdu(char **dict_p, char *nbr, int cdu);
void	def_dec(char **dict_p, char *nbr);

#endif
