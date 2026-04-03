def ft_count_harvest_recursive(n=0, max=int(input("Days until harvest: "))):
    if (n >= 0 and n < max):
        print("Day ", n + 1)
        ft_count_harvest_recursive(n + 1, max)
    if (n == max):
        print("Harvest time!")
