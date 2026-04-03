#include <stdlib.h>
#include <unistd.h>
#include "rush_02.h"
#include "lib/rs.h"

int	ft_print_dec_one(char **dict_p, char *nbr)
{
	int	x;

	x = 0;
	while(dict_p[x])
	{
		if (ft_atoi(dict_p[x]) == ft_atoi(nbr))
		{
			ft_putstr(dict_p[x + 1]);
			write(1, " ", 1);
			return (1);
		}
		x += 2;
	}
	return (0);
}

void ft_print_unit(char **dict_p, char unity)
{
	char unit[1];

	if(unity != 0)
	{
		unit[0] = unity;
		ft_print_dec_one(dict_p, unit);
	}
}

void	def_dec(char **dict_p, char *nbr)
{
	int	i;

	i = 0;
	if (nbr[0] != '1')
	{
		while (dict_p[i])
		{
			if (ft_strlen(dict_p[i]) == 2 && dict_p[i][0] == nbr[0])
			{
				ft_putstr(dict_p[i + 1]);
				write(1, " ", 1);
				ft_print_unit(dict_p, nbr[1]);
				break ;
			}
			i += 2;
		}
	}
	else
		ft_print_dec_one(dict_p, nbr);
}

void ft_create_dec(char **dict_p, char *nbr)
{
	char *nbr_cdu;

	nbr_cdu = malloc(sizeof(char) * 2);
	if(!nbr_cdu)
		free(nbr_cdu);
	nbr_cdu[0] = nbr[0];
	nbr_cdu[1] = nbr[1];
    if (ft_print_dec_one(dict_p, nbr_cdu) == 0)
	    def_dec(dict_p, nbr_cdu);
	free(nbr_cdu);
}

void	ft_print_cdu(char **dict_p, char *nbr, int cdu)
{
	int i;

	i = 0;
	if (cdu == 0)
	{
		ft_print_unit(dict_p, nbr[0]);
		while (dict_p[i])
		{
			if(ft_strlen(dict_p[i]) == 3 && dict_p[i][0] == '1')
				ft_putstr(dict_p[i + 1]);
			i += 2;
		}
		write(1, " ", 1);
		ft_create_dec(dict_p, nbr + 1);
		return ;
	}
	if(cdu == 2)
	{
		ft_create_dec(dict_p, nbr);
		return ;
	}
	ft_print_unit(dict_p, nbr[0]);
}