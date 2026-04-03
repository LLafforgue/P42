#include "../lib/rs.h"

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while(str[i])
	{
		write(1, &str[i], 1);
		i ++;
	}
}
/*
void	copy(char *str)
{
	int	size;
	char	*dup;
	int 	i;

	size = 0;
	i = 0;
	while(str[size])
	{
		size ++;
	}
	dup = (char *) malloc(sizeof(char) * (size + 1));
	if (dup == NULL)
		return (NULL);
	while(i < size)
	{
		dup[i] = str[i];
		i ++;
	}
	dup[i] = '\0';
	return (dup);
}
*/

unsigned	ft_atoi(char *number)
{
	unsigned	nbr;

    nbr = 0;
    while (*number < '!')
		number++;
	if (*number != '+' && !(*number >= '0' && *number <= '9'))
		return (0);
	else if (*number == '+')
		number++;
	while (*number >= '0' && *number <= '9')
	{
		nbr *= 10;
		nbr += *number - 48;
		number++;
	}
	return (nbr);
}
